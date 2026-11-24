"""
train_model.py
--------------
Standalone training script for Movie Review Sentiment Analysis.

Usage (from the aclImdb/ project root with the virtual environment active):
    python train_model.py

What this script does
~~~~~~~~~~~~~~~~~~~~~
1.  Loads the labelled IMDb training reviews (train/pos, train/neg).
2.  Cleans the review text (HTML removal, lowercase, etc.).
3.  Splits training data into train (80%) + validation (20%).
4.  Trains three models on TF-IDF features:
        a) Multinomial Naive Bayes
        b) Logistic Regression
        c) Linear Support Vector Machine (LinearSVC)
5.  Selects the best model based on validation F1-score (macro).
6.  Evaluates the selected model on the official held-out test set.
7.  Prints the classification report and confusion matrix.
8.  Saves the complete fitted Pipeline to models/sentiment_pipeline.joblib.

Data leakage prevention
~~~~~~~~~~~~~~~~~~~~~~~~
The TF-IDF vectorizer is part of the scikit-learn Pipeline.  It is fitted
ONLY on training data inside Pipeline.fit().  Validation and test data are
only transformed, never used to fit the vectorizer.
"""

import os
import sys

# Ensure immediate line-buffered output to terminal/logs
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)
import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for scripts
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    accuracy_score,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
DATASET_ROOT = SCRIPT_DIR                        # aclImdb/ is the project root
MODELS_DIR   = os.path.join(SCRIPT_DIR, "models")
MODEL_PATH   = os.path.join(MODELS_DIR, "sentiment_pipeline.joblib")

# Add src/ to path so we can import our modules
sys.path.insert(0, SCRIPT_DIR)
from src.data_loader   import load_imdb_dataset, get_train_test
from src.preprocessing import apply_cleaning

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
RANDOM_STATE = 42

# ---------------------------------------------------------------------------
# 1. Load dataset
# ---------------------------------------------------------------------------
print("=" * 60)
print("Movie Review Sentiment Analysis — Model Training")
print("=" * 60)
print(f"\n[1/7] Loading dataset from: {DATASET_ROOT}")

df = load_imdb_dataset(DATASET_ROOT)
train_df, test_df = get_train_test(df)

print(f"       Training reviews : {len(train_df):,}")
print(f"       Test reviews     : {len(test_df):,}")
print(f"       Train class dist :\n{train_df['sentiment'].value_counts().to_string()}")

# ---------------------------------------------------------------------------
# 2. Clean text
# ---------------------------------------------------------------------------
print("\n[2/7] Cleaning review text …")

# Keep original text; store cleaned version separately
train_df["clean_review"] = apply_cleaning(train_df["review"])
test_df["clean_review"]  = apply_cleaning(test_df["review"])

print("       Sample cleaned review (first 200 chars):")
print("      ", train_df["clean_review"].iloc[0][:200])

# ---------------------------------------------------------------------------
# 3. Train / validation split  (from training data only)
# ---------------------------------------------------------------------------
print("\n[3/7] Creating 80/20 train/validation split …")

X_train_full = np.array(train_df["clean_review"].tolist(), dtype=object)
y_train_full = np.array(train_df["label"].tolist(), dtype=int)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_full, y_train_full,
    test_size=0.20,
    random_state=RANDOM_STATE,
    stratify=y_train_full,
)

print(f"       Train samples : {len(X_train):,}")
print(f"       Val   samples : {len(X_val):,}")

# ---------------------------------------------------------------------------
# 4. Define models to compare
# ---------------------------------------------------------------------------
print("\n[4/7] Training and comparing models on validation set …")

# Shared TF-IDF settings:
#   - unigrams + bigrams
#   - sublinear_tf smooths extreme term frequencies
#   - min_df=2 drops very rare tokens
#   - max_features caps vocabulary size for memory
TFIDF_PARAMS = dict(
    ngram_range=(1, 2),
    sublinear_tf=True,
    min_df=2,
    max_features=100_000,
)

CANDIDATES = {
    "Multinomial Naive Bayes": Pipeline([
        ("tfidf", TfidfVectorizer(**TFIDF_PARAMS)),
        ("clf",   MultinomialNB(alpha=0.1)),
    ]),
    "Logistic Regression": Pipeline([
        ("tfidf", TfidfVectorizer(**TFIDF_PARAMS)),
        ("clf",   LogisticRegression(
            C=1.0,
            max_iter=1000,
            solver="lbfgs",
            random_state=RANDOM_STATE,
        )),
    ]),
    "Linear SVM": Pipeline([
        ("tfidf", TfidfVectorizer(**TFIDF_PARAMS)),
        ("clf",   LinearSVC(
            C=1.0,
            max_iter=2000,
            random_state=RANDOM_STATE,
        )),
    ]),
}

val_results = {}
for name, pipeline in CANDIDATES.items():
    pipeline.fit(X_train, y_train)
    y_pred_val = pipeline.predict(X_val)
    acc = accuracy_score(y_val, y_pred_val)
    f1  = f1_score(y_val, y_pred_val, average="macro")
    val_results[name] = {"accuracy": acc, "f1_macro": f1, "pipeline": pipeline}
    print(f"       {name:<30s}  val_acc={acc:.4f}  val_f1={f1:.4f}")

# ---------------------------------------------------------------------------
# 5. Select the best model (highest macro F1 on validation set)
# ---------------------------------------------------------------------------
best_name = max(val_results, key=lambda k: val_results[k]["f1_macro"])
best_pipeline = val_results[best_name]["pipeline"]

print(f"\n[5/7] Selected model : {best_name}")
print(f"       Val accuracy  : {val_results[best_name]['accuracy']:.4f}")
print(f"       Val F1 (macro): {val_results[best_name]['f1_macro']:.4f}")

# ---------------------------------------------------------------------------
# 6. Final evaluation on the official held-out test set
# ---------------------------------------------------------------------------
print("\n[6/7] Evaluating on official test set …")

X_test = np.array(test_df["clean_review"].tolist(), dtype=object)
y_test = np.array(test_df["label"].tolist(), dtype=int)

y_pred_test = best_pipeline.predict(X_test)

test_acc = accuracy_score(y_test, y_pred_test)
print(f"\n       Test Accuracy : {test_acc:.4f}")
print("\n       Classification Report:")
print(classification_report(
    y_test, y_pred_test,
    target_names=["Negative", "Positive"],
    digits=4,
))

# Confusion matrix plot
cm = confusion_matrix(y_test, y_pred_test)
fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=["Negative", "Positive"],
    yticklabels=["Negative", "Positive"],
    ax=ax,
)
ax.set_xlabel("Predicted Label")
ax.set_ylabel("True Label")
ax.set_title(f"Confusion Matrix — {best_name}\n(Official Test Set, n=25,000)")
plt.tight_layout()
cm_path = os.path.join(SCRIPT_DIR, "confusion_matrix.png")
fig.savefig(cm_path, dpi=120)
print(f"       Confusion matrix saved to: {cm_path}")

# ---------------------------------------------------------------------------
# 7. Save the fitted pipeline
# ---------------------------------------------------------------------------
print(f"\n[7/7] Saving pipeline to: {MODEL_PATH}")
os.makedirs(MODELS_DIR, exist_ok=True)
joblib.dump(best_pipeline, MODEL_PATH)
print("       Done. Pipeline saved successfully.")

print("\n" + "=" * 60)
print("Training complete!")
print(f"  Best model  : {best_name}")
print(f"  Test acc    : {test_acc:.4f}")
print(f"  Model file  : {MODEL_PATH}")
print("=" * 60)
print("\nTo launch the Streamlit application, run:")
print("  streamlit run app.py")
