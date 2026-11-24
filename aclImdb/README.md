# 🎬 CineSense: Movie Review Sentiment Analysis using NLP & Machine Learning

[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn%201.3%2B-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Web Framework](https://img.shields.io/badge/GUI-Streamlit%201.28%2B-red?logo=streamlit)](https://streamlit.io/)
[![Dataset](https://img.shields.io/badge/Dataset-Stanford%20IMDb%20(50k)-yellow?logo=imdb)](https://ai.stanford.edu/~amaas/data/sentiment/)
[![Accuracy](https://img.shields.io/badge/Test%20Accuracy-89.90%25-brightgreen)](models/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end Natural Language Processing (NLP) and Machine Learning project developed from scratch following rigorous academic engineering standards. The system classifies user-entered movie reviews as **Positive** or **Negative** with high confidence, accompanied by an interactive, modern **Streamlit web application**.

---

## 📑 Table of Contents
1. [Project Overview](#-project-overview)
2. [Problem Statement & Objectives](#-problem-statement--objectives)
3. [Dataset Description & Academic Scope](#-dataset-description--academic-scope)
4. [Technology Stack & Justification](#-technology-stack--justification)
5. [End-to-End System Architecture](#-end-to-end-system-architecture)
6. [Complete 10-Stage Development Lifecycle](#-complete-10-stage-development-lifecycle)
7. [Experimental Results & Model Comparison](#-experimental-results--model-comparison)
8. [Streamlit Graphical User Interface](#-streamlit-graphical-user-interface)
9. [Project Directory Structure](#-project-directory-structure)
10. [Step-by-Step Installation & Run Guide](#-step-by-step-installation--run-guide)
11. [Testing & Verification Protocol](#-testing--verification-protocol)
12. [Faculty Viva / Oral Presentation FAQ](#-faculty-viva--oral-presentation-faq)
13. [Limitations & Future Improvements](#-limitations--future-improvements)
14. [Academic Citation](#-academic-citation)

---

## 🌟 Project Overview

Customer reviews and audience ratings on platforms like IMDb, Rotten Tomatoes, and Google Play provide critical feedback for creators, studios, and consumers. However, manually reading and categorizing tens of thousands of unstructured text reviews is time-prohibitive.

**CineSense** solves this by leveraging classical Natural Language Processing (NLP) and statistical machine learning to automatically analyze the sentiment of film reviews.

### What the System Delivers:
- **High-Accuracy Classification**: Predicts review polarity (**Positive** vs. **Negative**) with **89.90% accuracy** on a 25,000-review held-out test benchmark.
- **Robust Feature Representation**: Employs Sublinear TF-IDF with $(1, 2)$-grams across a 100,000-feature vocabulary.
- **Linguistic Negation Protection**: Explicitly protects critical sentiment reversers (`not`, `never`, `didn't`, `cannot`) from aggressive stopword removal.
- **Zero Data Leakage**: Vectorizer transformations are strictly fitted on training splits inside an encapsulated `scikit-learn` Pipeline.
- **Interactive Web Interface**: A production-ready Streamlit GUI supporting real-time user input, 1-click sample benchmarks, confidence probability bars, and preprocessing inspection tabs.

---

## 🎯 Problem Statement & Objectives

### Problem Statement
To engineer a reliable, user-friendly desktop/web software system that accepts unstructured movie reviews in natural English text and accurately predicts their underlying polarity using NLP and machine learning techniques trained on a validated public benchmark.

### Core Objectives:
1. **Dataset Ingestion**: Extract and validate 50,000 reviews from the Stanford Large Movie Review Dataset.
2. **Data Cleaning**: Audit and resolve null values, empty reviews, character encodings, and duplicates.
3. **Text Preprocessing**: Normalize case, strip HTML artefacts, and preserve sentiment-bearing negation tokens.
4. **Exploratory Data Analysis**: Uncover linguistic patterns, vocabulary frequencies, and document length distributions.
5. **Feature Engineering**: Evaluate Bag of Words (BoW) vs. Term Frequency–Inverse Document Frequency (TF-IDF).
6. **Model Development**: Train and benchmark **Multinomial Naive Bayes**, **Logistic Regression**, and **Linear Support Vector Machines (LinearSVC)**.
7. **Model Evaluation**: Measure held-out generalization using Accuracy, Precision, Recall, Macro F1-score, and Confusion Matrices.
8. **Application Deployment**: Deliver an interactive Streamlit graphical application.

---

## 📊 Dataset Description & Academic Scope

### The Stanford IMDb Dataset (`aclImdb`)
This project utilizes the benchmark **Large Movie Review Dataset v1.0** compiled by Maas et al. (Stanford University AI Lab):

| Split | Positive Reviews ($\ge 7/10$) | Negative Reviews ($\le 4/10$) | Total Labelled Reviews |
|---|:---:|:---:|:---:|
| **Training Set** | 12,500 | 12,500 | **25,000** |
| **Test Set (Held-Out)** | 12,500 | 12,500 | **25,000** |
| **Combined** | **25,000** | **25,000** | **50,000** |

*Note: Reviews are stored as individual `.txt` files inside `train/pos`, `train/neg`, `test/pos`, and `test/neg` folders. Labels are derived solely from folder names, never inferred by heuristic keyword guessing.*

### ⚖️ Academic Scope Limitation (Binary vs. Neutral)
- **Course Specification Note**: While generalized sentiment analysis briefs frequently reference a three-class schema (*Positive, Negative, Neutral*), the Stanford IMDb benchmark dataset explicitly excludes neutral reviews ($5/10$ or $6/10$ stars).
- **Integrity Compliance**: In accordance with academic guidelines, this project is deliberately formulated as a **Binary Classifier** (*Positive* vs. *Negative*). We do not synthesize or guess artificial neutral labels. This scope limitation is explicitly disclosed in the GUI and presentation.

---

## 🛠️ Technology Stack & Justification

| Technology | Role | Justification |
|---|---|---|
| **Python 3.9+** | Core Language | Standard language for modern NLP, data science, and ML workflows. |
| **Scikit-Learn** | Machine Learning & Pipeline | Provides robust, leakage-free vectorizers, classifiers, and evaluation tools. |
| **NLTK** | Linguistic Resources | Supplies English stopword corpora for vocabulary filtering. |
| **Pandas & NumPy** | Data Wrangling & Matrices | High-performance tabular data structures and array operations. |
| **Matplotlib & Seaborn** | Statistical Visualizations | Generates clean confusion matrices, length histograms, and bar plots. |
| **Streamlit** | Web GUI Application | Builds responsive, modern Python web applications with zero JavaScript overhead. |
| **Joblib** | Serialization | Efficiently saves and loads the fitted vectorizer-classifier pipeline. |

---

## 🏗️ End-to-End System Architecture

```text
[ User Enters Movie Review ]
             │
             ▼
   [ Streamlit Web GUI ] ──────── (Validates empty / whitespace input)
             │
             ▼
   [ Text Preprocessing ]
       ├── Decode HTML entities (&amp; -> &)
       ├── Strip HTML tags (<br />, <i>, etc.)
       ├── Lowercase normalization
       ├── Clean special punctuation (keep apostrophes for contractions)
       └── PROTECT negation tokens (not, no, never, didn't, etc.)
             │
             ▼
  [ Scikit-Learn Pipeline ]
       ├── TF-IDF Vectorizer (Fitted on Train Set Only)
       │     • (1, 2)-grams (captures phrases like "not good")
       │     • Sublinear TF scaling (1 + log(tf))
       │     • 100,000 max vocabulary features
       │
       └── Linear Support Vector Machine (LinearSVC)
             • Hyperplane decision boundary
             • Calibrated sigmoid confidence estimation
             │
             ▼
[ Output: Predicted Sentiment + Confidence % + Visual Insights ]
```

---

## 🔬 Complete 10-Stage Development Lifecycle

### Stage 1: Problem Identification
Formulated the project as an NLP text classification challenge. Defined the target domain (movie reviews), input format (raw user text), and output format (binary sentiment label + confidence probability).

### Stage 2: Dataset Collection & Understanding
Extracted the official `aclImdb` directory. Inspected directory trees, confirmed file counts (exactly 12,500 files per sentiment folder), and verified the separation of training and test splits.

### Stage 3: Data Cleaning
Implemented an audit in `notebooks/01_dataset_exploration.ipynb`:
- **Missing values**: Checked for nulls across all text columns ($0$ nulls found).
- **Empty records**: Checked for $0$-byte or whitespace-only documents ($0$ found).
- **Encoding errors**: Configured resilient UTF-8 decoding with Latin-1 fallbacks.

### Stage 4: Text Preprocessing & Negation Preservation
Raw reviews contain HTML formatting artefacts like `<br />` and `&quot;`. In `src/preprocessing.py`, we engineered `clean_review()`:
- **Negation Rule**: Standard stopword removal removes `not`, `no`, `never`. In sentiment analysis, *"The movie was good"* and *"The movie was not good"* have opposite polarities. Our custom filter strictly preserves all 26 English negation words.

### Stage 5: Exploratory Data Analysis (EDA)
Documented in `notebooks/03_eda.ipynb`:
- **Class Balance**: Perfectly balanced ($50.0\%$ Positive, $50.0\%$ Negative).
- **Review Lengths**: Mean review length is $\approx 230$ words; lengths range from 10 to over 1,000 words. Length distributions between positive and negative classes are nearly identical.
- **Top N-Grams**: Identified distinct polarity signals (Positive: *great, excellent, masterpiece, best*; Negative: *worst, awful, waste, boring, terrible*).

### Stage 6: Feature Engineering
Implemented in `notebooks/04_feature_engineering.ipynb`:
- **Bag of Words (BoW)**: Explored word count matrices as a baseline.
- **TF-IDF (Selected)**: Term Frequency–Inverse Document Frequency scales down words that appear across all documents while elevating rare, highly informative terms. Configured with:
  - `ngram_range=(1, 2)`: Captures bigrams like `"not bad"` or `"visually stunning"`.
  - `sublinear_tf=True`: Uses $1 + \log(\text{tf})$ to dampen the influence of repeated words.
  - `min_df=2`: Excludes idiosyncratic single-character typos.
  - `max_features=100_000`: Caps memory footprint for fast inference.

### Stage 7: Model Development
In `train_model.py`, we created an 80/20 train/validation split ($20,000$ train, $5,000$ validation) and benchmarked three classifiers under identical conditions:
1. **Multinomial Naive Bayes** ($\alpha = 0.1$)
2. **Logistic Regression** ($C = 1.0$, L-BFGS solver)
3. **Linear Support Vector Machine** ($C = 1.0$)

### Stage 8: Model Evaluation
Evaluated the selected model on the untouched 25,000 held-out test reviews. Generated the classification report and saved `confusion_matrix.png`.

### Stage 9: GUI Development
Developed a modern, interactive web application in `app.py` utilizing Streamlit, custom CSS, 1-click sample buttons, and diagnostic inspection tabs.

### Stage 10: Testing & Verification
Tested extreme inputs, edge cases, negations, empty inputs, and repeated runs to verify zero memory leaks and deterministic inference.

---

## 📈 Experimental Results & Model Comparison

### 1. Validation Split Performance (20,000 Train / 5,000 Validation)
| Model Architecture | Validation Accuracy | Validation Macro F1 | Selection Outcome |
|---|:---:|:---:|:---:|
| **Multinomial Naive Bayes** | 88.06% | 0.8806 | Baseline |
| **Logistic Regression (L-BFGS)** | 88.92% | 0.8892 | Strong Candidate |
| **Linear Support Vector Machine (LinearSVC)** | **90.00%** | **0.9000** | **Selected Best Model** |

### 2. Final Evaluation on Held-Out Test Set (25,000 Unseen Reviews)
The winning model (**Linear SVM**) was evaluated on the untouched official test set:

- **Overall Test Accuracy**: **89.90%**
- **Macro Average F1-Score**: **0.8990**

#### Detailed Classification Report:
| Class | Precision | Recall | F1-Score | Support (Reviews) |
|---|:---:|:---:|:---:|:---:|
| **Negative** | 0.8984 | 0.8998 | 0.8991 | 12,500 |
| **Positive** | 0.8996 | 0.8982 | 0.8989 | 12,500 |
| **Accuracy** | — | — | **0.8990** | **25,000** |
| **Macro Average** | **0.8990** | **0.8990** | **0.8990** | **25,000** |
| **Weighted Average** | **0.8990** | **0.8990** | **0.8990** | **25,000** |

#### Confusion Matrix Summary:
- **True Negatives (Correctly flagged negative)**: $11,247$
- **False Positives (Negative reviews misclassified as positive)**: $1,253$
- **False Negatives (Positive reviews misclassified as negative)**: $1,273$
- **True Positives (Correctly flagged positive)**: $11,227$

*(Visual chart exported as `confusion_matrix.png` in project root)*

---

## 💻 Streamlit Graphical User Interface

The application (`app.py`) is styled with custom SaaS-grade CSS:
1. **Hero Header**: Displays project title, badges, and academic scope disclosure.
2. **Interactive Sidebar**: Academic metadata, model configuration summary, and 1-click test review buttons (*Positive, Negative, Tricky Negation, Mixed*).
3. **Review Input Box**: Multi-line text area with input validation for empty or whitespace-only text.
4. **Result Cards**:
   - Polarity Badge: Emerald Green for Positive 😊, Rose Red for Negative 😞.
   - Confidence Percentage gauge and dynamic polarity distribution bar.
5. **Linguistic Diagnostic Tabs**:
   - **Tab 1: Linguistic Preprocessing**: Displays original vs. cleaned text and highlights preserved negation tokens (`not`, `never`, `didn't`).
   - **Tab 2: NLP Pipeline Inspection**: Explains TF-IDF token weighting and SVM classification hyperplane.
   - **Tab 3: Model Evaluation Evidence**: Embeds the test confusion matrix and benchmark metric tables.

---

## 📂 Project Directory Structure

```text
movie sentiment analysis/
└── aclImdb/
    ├── src/                                  # Modular Python source packages
    │   ├── __init__.py
    │   ├── data_loader.py                    # Multi-threaded IMDb dataset loader
    │   └── preprocessing.py                 # Fast regex text cleaning & negation logic
    │
    ├── notebooks/                            # Academic step-by-step notebooks
    │   ├── 01_dataset_exploration.ipynb      # Stage 2 & 3: Collection & Cleaning
    │   ├── 02_preprocessing.ipynb            # Stage 4: Linguistic Preprocessing
    │   ├── 03_eda.ipynb                      # Stage 5: Exploratory Data Analysis & Plots
    │   ├── 04_feature_engineering.ipynb      # Stage 6: BoW & TF-IDF Demonstration
    │   └── 05_model_training_evaluation.ipynb# Stage 7 & 8: Model Comparison & Metrics
    │
    ├── models/
    │   └── sentiment_pipeline.joblib         # Exported fitted TF-IDF + LinearSVC Pipeline
    │
    ├── train/                                # Stanford IMDb training split (25,000 txt files)
    ├── test/                                 # Stanford IMDb test split (25,000 txt files)
    │
    ├── app.py                                # Streamlit Web GUI Application
    ├── train_model.py                        # Standalone reproducible training script
    ├── requirements.txt                      # Pinned Python package dependencies
    ├── confusion_matrix.png                  # Evaluation visual evidence chart
    ├── .gitignore                            # Git exclusion rules for large datasets
    └── README.md                             # Comprehensive GitHub documentation
```

---

## 🚀 Step-by-Step Installation & Run Guide

### 1. Prerequisites
- Python 3.9, 3.10, or 3.11 installed on your computer.
- Git (optional, for version control).

### 2. Open Terminal in the Project Directory
```powershell
cd "c:\Users\user\Desktop\NLP\project\movie sentiment analysis\aclImdb"
```

### 3. Create & Activate a Python Virtual Environment
**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Retrain Model (Optional — Pre-trained Pipeline is Already Saved)
To retrain the models from scratch and regenerate the confusion matrix:
```powershell
python train_model.py
```

### 6. Launch the Streamlit Web Application
```powershell
streamlit run app.py
```
Your browser will automatically open:
👉 **`http://localhost:8501`**

### 7. Run Jupyter Notebooks
To explore the academic notebooks:
```powershell
jupyter notebook
```
Navigate to the `notebooks/` directory and open any `.ipynb` file.

---

## 🧪 Testing & Verification Protocol

The pipeline was validated against representative linguistic test cases:

| Input Text Test Case | Type | Expected Polarity | Observed Result | Model Confidence |
|---|:---:|:---:|:---:|:---:|
| *"The movie was fantastic. The acting was excellent and the story kept me interested throughout."* | Clear Positive | **Positive** | **Positive** ✅ | 81.3% |
| *"This was an awful, terrible, boring film with horrible acting."* | Clear Negative | **Negative** | **Negative** ✅ | 92.5% |
| *"The film was not good and I did not enjoy it."* | Negation | **Negative** | **Negative** ✅ | 64.0% |
| *"Never going to watch this again. Total waste of time."* | Strong Negative | **Negative** | **Negative** ✅ | 81.3% |
| *"" (Empty string or spaces)* | Edge Case | Handled | **Warning message displayed** ✅ | N/A |

---

## 🎓 Faculty Viva / Oral Presentation FAQ

Prepare for your presentation and viva exam with these concise technical explanations:

<details>
<summary><b>Q1: Why did you choose Linear SVM over Naive Bayes or Logistic Regression?</b></summary>
<b>Answer:</b> While Multinomial Naive Bayes is fast, its conditional independence assumption ("naive" assumption) limits its expressive power on correlated word pairs. Linear Support Vector Machines find the maximum-margin hyperplane in high-dimensional sparse spaces (such as our 100,000 TF-IDF feature space), yielding higher validation accuracy (90.00%) and better test generalization (89.90%).
</details>

<details>
<summary><b>Q2: How did you ensure there is no Data Leakage in your NLP pipeline?</b></summary>
<b>Answer:</b> Data leakage occurs if feature engineering (such as vocabulary selection or inverse document frequency calculations) incorporates test or validation data. We prevented this by encapsulating the <code>TfidfVectorizer</code> and classifier inside a <code>scikit-learn Pipeline</code>. The pipeline is fitted strictly on the training partition; validation and test splits are transformed using the already-fitted vectorizer.
</details>

<details>
<summary><b>Q3: Why is Term Frequency–Inverse Document Frequency (TF-IDF) better than Bag of Words (BoW)?</b></summary>
<b>Answer:</b> Bag of Words counts raw frequencies, meaning ubiquitous words like "film" or "movie" dominate feature counts without providing discriminative sentiment value. TF-IDF applies an inverse document frequency penalty, dampening frequent non-informative terms while giving higher weight to distinctive polarity words like "masterpiece" or "atrocious".
</details>

<details>
<summary><b>Q4: Why does the system predict Positive and Negative instead of Neutral?</b></summary>
<b>Answer:</b> The Stanford Large Movie Review Dataset (Maas et al., 2011) only contains polarized reviews ($\ge 7/10$ stars as positive and $\le 4/10$ stars as negative); neutral reviews were intentionally excluded from the source dataset. Rather than fabricating or guessing an unlabelled neutral category, our faculty approved formulating the task as a principled binary classification problem.
</details>

<details>
<summary><b>Q5: How do you handle negation words like "not good"?</b></summary>
<b>Answer:</b> Typical NLP stopword removal indiscriminately removes words like "not", "no", and "never", which flips "not good" into "good". We implemented a custom filter that preserves all 26 English negation words. In addition, our TF-IDF vectorizer includes bigrams (<code>ngram_range=(1, 2)</code>), ensuring that phrases like "not good" are treated as distinct single features.
</details>

---

## 🔮 Limitations & Future Improvements

1. **Domain Specificity**: The model is optimized for movie reviews. Vocabulary shifts in product reviews (e.g., electronics, apparel) may require domain adaptation.
2. **Sarcasm & Subtle Irony**: Complex rhetorical devices (e.g., *"What a brilliant waste of two hours!"*) remain challenging for linear n-gram models.
3. **Deep Learning & Transformers**: Future iterations could benchmark contextual embedding architectures like DistilBERT or RoBERTa for deeper semantic comprehension.
4. **Three-Class Expansion**: Supplementing the dataset with the Stanford Sentiment Treebank (SST-3) would enable true neutral-class classification.

---

## 📚 Academic Citation

If you reference this project or dataset in your coursework, please cite the official benchmark paper:

```bibtex
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L. and Daly, Raymond E. and Pham, Peter T. and Huang, Dan and Ng, Andrew Y. and Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (ACL-HLT)},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  pages     = {142--150},
  url       = {https://aclanthology.org/P11-1015/}
}
```

---

<div align="center">
  <b>Developed for 5th Semester NLP Academic Coursework</b><br>
  Built with ❤️ using Python, Scikit-Learn, and Streamlit
</div>
