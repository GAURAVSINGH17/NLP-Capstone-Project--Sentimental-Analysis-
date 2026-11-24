# PROJECT SPECIFICATION: Sentiment Analysis (Positive / Negative / Neutral)

> **To the AI agent reading this file:** This document is a complete specification for a college project. Read it fully before writing any code. Build the entire project from scratch in this folder, following the stages in order, and verify everything works before you finish. The "Definition of Done" (Section 12) tells you when you are finished.

---

## 1. Context: who this is for and why it matters

- The owner is a **college student who is new to NLP/ML**.
- This is a **college project** that will be evaluated by faculty. The student must **explain every part in a viva and a presentation**.
- Therefore the code and notebook must be:
  - **Simple and readable** (no over-engineering, no clever one-liners the student cannot explain).
  - **Well commented** and accompanied by **plain-English Markdown explanations** in the notebook ("what this step does" and "why we do it").
  - Built using the **exact stages and requirements** given by the faculty (Section 2).
- The student prefers working in a **Jupyter Notebook** for the learning/building stages, but the faculty requires a **working GUI**, so the final project is **notebook + Streamlit app**.

---

## 2. Faculty requirements (verbatim, these are mandatory)

### Project Brief: Sentiment Analysis

**Objective:** Build a system that identifies whether a given sentence, review, or feedback is positive, negative, or neutral.

**What you have to build:**
- Collect movie or product reviews.
- Clean and preprocess the text.
- Convert text into numerical features using techniques such as TF-IDF.
- Train a machine learning classification model.
- Predict the sentiment of new user-entered text.

**Suggested dataset:** IMDb Movie Reviews.

**GUI features:**
- Text input box for a review.
- Predict Sentiment button.
- Display Positive, Negative, or Neutral result.
- Show prediction confidence, if supported.

**Expected output:** A sentiment prediction application where users can enter any review and view its predicted sentiment.

### Complete Project Development

Each project must be developed from scratch and should cover the following stages:
1. **Problem Identification:** Understand the problem statement, objectives and real-world applications.
2. **Dataset Collection:** Find, download and understand the relevant dataset.
3. **Data Cleaning:** Handle missing values, duplicates and inconsistent data.
4. **Text Preprocessing:** Perform tokenization, normalization, stopword removal, stemming or lemmatization wherever required.
5. **EDA:** Perform exploratory data analysis and visualize important patterns.
6. **Feature Engineering:** Apply suitable NLP techniques such as Bag of Words, TF-IDF, Word2Vec or embeddings.
7. **Model Development:** Select, train and test suitable ML/DL/NLP models.
8. **Model Evaluation:** Evaluate performance using appropriate metrics such as Accuracy, Precision, Recall and F1-score.
9. **GUI Development:** Build a user-friendly interface using Streamlit or any other suitable web technology.
10. **Testing & Implementation:** Test the complete application and ensure that it works properly from input to final output.

### Mandatory Requirement
Every project must have a working GUI or web-based interface. **A Jupyter Notebook alone will not be accepted as a complete project.**

---

## 3. Dataset (already provided)

- **Name:** IMDb Large Movie Review Dataset (`aclImdb_v1`).
- **Location:** The archive `aclImdb_v1.tar.gz` (the student's copy may be named `aclImdb_v1_tar.gz`) is in the project root. If the folder `aclImdb/` does not exist yet, **extract the archive** into the project root (`tar -xzf <archive>`). Do not re-download if the archive or folder exists.
- **Expected structure:**

```
aclImdb/
├── train/
│   ├── pos/    12,500 .txt files  (ratings 7-10)
│   ├── neg/    12,500 .txt files  (ratings 1-4)
│   └── unsup/  50,000 unlabeled files  -> IGNORE, do not use
└── test/
    ├── pos/    12,500 .txt files
    └── neg/    12,500 .txt files
```

- **Format:** each review is a separate text file named `<reviewID>_<rating>.txt` (e.g. `127_3.txt` = review 127, rating 3 out of 10). Read the rating from the file name.
- **Size:** 50,000 labelled reviews (25,000 train + 25,000 test), perfectly balanced between positive and negative.
- **Encoding:** read files with `encoding="utf-8"`.
- **Noise to expect:** HTML tags such as `<br />`, duplicates, mixed case, punctuation, apostrophes.
- **Ratings 5 and 6 do not exist** in this dataset (removed by the creators).

---

## 4. KEY DESIGN DECISION: how to get "Neutral"

**Problem:** IMDb contains **only Positive and Negative** reviews. There is no Neutral label, but the faculty requires the app to show Positive, Negative **or** Neutral.

**Chosen solution (do exactly this):**
1. Train a **binary** classifier (Positive vs Negative) that outputs class probabilities.
2. In prediction, take the **highest class probability** (the "confidence").
3. If `confidence < THRESHOLD`, the model is unsure between the two classes, so the text is mixed or neutral, and the app outputs **Neutral**. Otherwise output the predicted class.
4. Choose `THRESHOLD` using the **validation set** (never the test set), in the range **0.60 to 0.75**, with a written justification (see Stage 8).
5. Save the chosen threshold in `artifacts/config.json` so the notebook, app and tests all use the same value. **Do not hard-code it in several places.**

**Evidence that this works (must be included, Stage 8):** A chart of average model confidence per original star rating. Borderline ratings (4 and 7) should show lower confidence than extreme ratings (1, 2, 9, 10). Also test with hand-written neutral and mixed sentences.

**Honesty requirement:** The notebook, report and app must clearly state that Neutral is derived from low confidence, not from true neutral labels, and that precision/recall/F1 are computed for Positive/Negative only. Do not claim a measured "Neutral accuracy".

---

## 5. Technology stack

| Purpose | Tool |
|---|---|
| Language | Python 3.9+ |
| Notebook | Jupyter (`sentiment_analysis.ipynb`) |
| Data handling | pandas, numpy |
| Text processing | NLTK (stopwords, WordNet lemmatizer) and `re` |
| Charts | matplotlib, seaborn, wordcloud (optional) |
| Features, models, metrics | scikit-learn |
| Saving models | joblib |
| GUI | Streamlit |
| Testing | pytest, `streamlit.testing.v1.AppTest` |

Create `requirements.txt` with the libraries above (pin versions that you actually installed and tested). Use a virtual environment if convenient.

---

## 6. Required project structure

```
sentiment_project/
├── aclImdb/                    # dataset (extracted)
├── sentiment_analysis.ipynb    # Stages 1-8 and 10, fully executed with outputs saved
├── preprocess.py               # preprocess(text) function (shared)
├── predict.py                  # load_artifacts(), predict_sentiment() (shared)
├── app.py                      # Streamlit GUI (Stage 9)
├── artifacts/
│   ├── tfidf.joblib
│   ├── model.joblib
│   ├── config.json             # {"threshold": ..., "model": "Logistic Regression", ...}
│   └── metrics.json            # test accuracy/precision/recall/F1 (for the app's info tab)
├── outputs/                    # saved charts + model_comparison.csv + classification_report.txt
├── tests/
│   └── test_project.py         # automated tests (Stage 10)
├── requirements.txt
├── README.md                   # short project README for submission (see Section 11)
├── REPORT.md                   # project report covering all 10 stages (Section 11)
└── VIVA_QA.md                  # likely viva questions with simple answers (Section 11)
```

**Why shared `preprocess.py` and `predict.py`:** the notebook, the app and the tests must clean and score text in exactly the same way. This prevents training/serving mismatch, and the student can explain it in the viva.

---

## 7. Step-by-step build plan (follow in order)

Work stage by stage. After each stage, **run the code and check the output** before moving on. In the notebook, every stage must have:
- a Markdown heading (`## Stage N: Name`),
- a Markdown cell explaining **what** this stage does and **why**,
- code cells with comments,
- a short Markdown **observation/summary** after the outputs (what we learned).

### Stage 0: Setup
- Extract the dataset if needed. Create `requirements.txt`, `artifacts/`, `outputs/`, `tests/`.
- Download required NLTK data (`stopwords`, `wordnet`) with `quiet=True`.
- Set `random_state=42` everywhere so results are reproducible.

### Stage 1: Problem Identification (Markdown cell only)
Write in simple language:
- the problem (free text is hard to analyse at scale),
- objective (classify text as Positive / Negative / Neutral),
- real-world applications (product and movie review analysis, brand monitoring, customer feedback and support prioritisation, social media analysis),
- the overall approach (pipeline diagram in text: text -> clean -> preprocess -> TF-IDF -> Logistic Regression -> confidence -> label -> Streamlit),
- the Neutral design decision (Section 4).

### Stage 2: Dataset Collection
- Write `load_split(split)` that walks `aclImdb/<split>/pos` and `neg`, reading each file and extracting `review`, `rating` (from the file name) and `sentiment` ("Positive" / "Negative").
- Build `train_df` and `test_df` (expected 25,000 rows each before cleaning).
- Show `shape`, `head()`, `sample()`, column meanings and class counts.
- Explain in Markdown: source, size, structure, labels, that ratings 5-6 are absent, and that `unsup` is ignored.

### Stage 3: Data Cleaning
- Check missing values (`isna().sum()`), count and **remove duplicate reviews** (by `review` text), remove empty or whitespace-only reviews, verify ratings are only in {1,2,3,4,7,8,9,10} (inconsistent-data check).
- **Also remove from the test set any review whose text also appears in the training set** (prevents leakage).
- Print counts before and after each cleaning step in a small summary table.
- Do not remove HTML tags here, that is done in Stage 4.

### Stage 4: Text Preprocessing
Implement `preprocess(text)` in `preprocess.py` and import it in the notebook. Steps, in order:
1. **Normalization:** lowercase.
2. Remove HTML tags (`<br />`, etc.) and URLs.
3. Expand contractions: `won't` -> `will not`, `can't` -> `can not`, `n't` -> ` not`.
4. **Tokenization:** extract word tokens with a regular expression (letters only).
5. **Stopword removal** using NLTK's English list, **but keep negation and intensity words** such as `no, nor, not, never, very, too, but, against`. (Removing "not" would turn "not good" into "good", a serious error.)
6. Drop 1-character tokens.
7. **Lemmatization** with `WordNetLemmatizer` (chosen over stemming because it returns real words).
8. Return the tokens joined by a space.

Requirements:
- Show a **before/after example** of 3 reviews, and a demonstration that "This is NOT good" keeps `not`.
- Include a short Markdown comparison of stemming vs lemmatization (optionally demo `PorterStemmer` on a few words, but do not use it in the pipeline).
- Apply to both `train_df` and `test_df` into a `clean` column. This is slow (a few minutes), so **cache** the cleaned data (e.g. `outputs/clean_train.csv`) and reload it if it exists, so re-runs are fast.
- After preprocessing, drop rows where `clean` is empty.

### Stage 5: EDA
Create and save (to `outputs/`, dpi=120) at least these charts, each followed by a written observation:
1. Sentiment class distribution (countplot).
2. Rating distribution (shows that 5 and 6 are missing).
3. Review length (word count) by sentiment (boxplot).
4. Top 15 words per sentiment (after preprocessing).
5. (Optional) WordCloud for each class.

Observations must be data-driven (for example: classes are balanced so accuracy is a fair metric; "movie"/"film" are frequent in both classes so they carry little signal).

### Stage 6: Feature Engineering
- Split `train_df` into **80% train / 20% validation** (`stratify`, `random_state=42`). The official `test_df` stays untouched until final evaluation.
- Explain **Bag of Words**, **TF-IDF** (TF x IDF), and mention **Word2Vec/embeddings** as alternatives, with the reason TF-IDF is chosen (fast, strong baseline for this task, required by the brief).
- Use `TfidfVectorizer(ngram_range=(1,2), min_df=3, max_features=100000, sublinear_tf=True)`.
- **`fit_transform` on the training split only; `transform` for validation and test.** State this explicitly (data leakage).
- Print the matrix shape and show the top-weighted terms for one example review.
- (Optional but valuable) Compare Bag of Words vs TF-IDF validation accuracy in a small table.

### Stage 7: Model Development
- Train and compare at least these three models on the TF-IDF features:
  - `LogisticRegression(max_iter=1000, C=2.0)`
  - `MultinomialNB()`
  - `LinearSVC()`
- Compare on the **validation set** with Accuracy, Precision, Recall, F1 (Positive as the positive class). Save `outputs/model_comparison.csv` and display the table.
- **Select Logistic Regression** for the app because the Neutral logic needs `predict_proba`, and Logistic Regression gives well-behaved probabilities. Explain this choice in Markdown.
- (Optional) light hyperparameter tuning of `C` using the validation set.
- After choosing the model, you may **refit on the full training data** (train + validation) before the final test evaluation; if you do, say so and refit the TF-IDF on the same full training data.

### Stage 8: Model Evaluation
**8a. Final evaluation on the test set (use it once):**
- Accuracy, Precision, Recall, F1 per class (`classification_report`), and a **confusion matrix** (saved to `outputs/confusion_matrix.png`). Save the report text to `outputs/classification_report.txt` and the numbers to `artifacts/metrics.json`.
- Explain each metric in simple words, with a mini-example.
- Expected accuracy is roughly **88-90%** for this setup. If your result is below about 85%, investigate (leakage checks, preprocessing, parameters) rather than ignoring it. Report whatever honest number you get.

**8b. Neutral threshold, with evidence:**
- Compute confidence (`predict_proba(...).max(axis=1)`) on the **validation set**, try thresholds 0.55 to 0.75, and report for each: the % of all reviews that would become Neutral, and the % of borderline-rating (4 and 7) reviews that become Neutral.
- Choose the threshold that labels borderline reviews as Neutral noticeably more often than clear reviews while keeping the Neutral share modest (a typical good value is 0.60-0.70). Justify the choice in Markdown.
- Plot **average confidence by star rating** (using the test set, for illustration only) and save as `outputs/confidence_by_rating.png`.
- Save the threshold to `artifacts/config.json`.

**8c. Qualitative check:** run at least 10 hand-written sentences (clearly positive, clearly negative, neutral such as "It was okay, nothing special", mixed such as "Good acting but the story was weak", and negation such as "Not good at all") and show the label and confidence in a table.

**8d. Limitations (Markdown):** no true neutral labels (cannot measure Neutral accuracy), sarcasm, domain shift (movie reviews vs product reviews), short text.

**Save artifacts:** `artifacts/tfidf.joblib`, `artifacts/model.joblib`, `artifacts/config.json`, `artifacts/metrics.json`.

### Stage 9: GUI Development (Streamlit, `app.py`)

**Shared logic in `predict.py`:**

```python
# predict.py (outline, implement properly)
def load_artifacts():           # loads tfidf, model, config from artifacts/ with relative paths
def predict_sentiment(text, tfidf, model, threshold):
    # 1) cleaned = preprocess(text)
    # 2) if cleaned is empty OR has no word known to the TF-IDF vocabulary
    #       -> return ("Neutral", confidence=None/0, probs=None, note="Not enough meaningful text")
    # 3) probs = model.predict_proba(tfidf.transform([cleaned]))[0]
    # 4) top = probs.argmax(); conf = probs[top]
    # 5) label = "Neutral" if conf < threshold else model.classes_[top]
    # 6) return label, conf, dict(zip(model.classes_, probs)), note
```

Step 2 matters: gibberish like "asdfgh" or "!!!" produces an all-zero feature vector, and the model would then return a meaningless probability. The app must handle this gracefully, not crash and not show a fake confident result.

**`app.py` must have (mandatory GUI features from the brief):**
- A **text input box** (`st.text_area`) for the review.
- A **"Predict Sentiment" button**.
- A clearly displayed result: **Positive**, **Negative** or **Neutral** (with an emoji and colour).
- The **prediction confidence** (percentage).

**Also include (for a polished demo):**
- A probability bar chart (Positive vs Negative).
- A friendly message when the result is Neutral explaining that the model is unsure between Positive and Negative.
- A warning for empty input, and a note for too-little-text input.
- A few clickable **example reviews** (positive, negative, neutral/mixed) that fill the text box.
- An **"About / Model performance" tab** showing: how it works (pipeline in 4-5 lines), the model comparison table, test accuracy/precision/recall/F1 from `metrics.json`, the confusion matrix image, the confidence-by-rating chart, and the **limitations** note (Neutral from confidence).
- Cache loading with `@st.cache_resource`.
- Relative paths only, so it runs from the project folder with `streamlit run app.py`.

### Stage 10: Testing & Implementation
Write `tests/test_project.py` (pytest) covering:
- `preprocess` keeps `not`, strips HTML and URLs, lowercases, lemmatizes ("movies" -> "movie").
- Clearly positive text -> Positive, clearly negative text -> Negative, "Not good at all" -> Negative.
- A neutral/mixed sentence returns Neutral **or** a confidence close to the threshold (document the observed behaviour; do not weaken the test to hide a failure, instead explain it).
- Empty text and gibberish do not crash and do not return a confident Positive/Negative.
- Probabilities sum to 1; confidence is between 0 and 1.
- A very long review (500+ words) works.
- A **GUI smoke test** using `streamlit.testing.v1.AppTest.from_file("app.py")`: app loads with no exception, entering text and clicking the button shows a result.

Also run the **notebook end to end** to confirm it executes without errors, for example:

```bash
jupyter nbconvert --to notebook --execute --inplace sentiment_analysis.ipynb
```

In the notebook's last section, include a **manual test table** (input, expected, actual, pass/fail) for the cases above. Where possible, capture screenshots of the running app (Positive, Negative, Neutral, empty input) and save them in `outputs/screenshots/`. If you cannot take screenshots in your environment, say so in your final message and describe the exact steps for the student to do it.

---

## 8. Rules and quality constraints

**Must do**
- Follow the 10 stages in order and keep them labelled the same way as the faculty list.
- Keep negation words (`not`, `no`, `never`) in preprocessing.
- Fit TF-IDF and the model on training data only. Touch the test set only for the final evaluation.
- Use `random_state=42` for reproducibility.
- Use relative paths (the project must run on the student's laptop, including Windows).
- Make the notebook run top to bottom with "Run All" and **save it with outputs visible**.
- Explain results honestly, including weaknesses.

**Must not do**
- Do not use `unsup` data.
- Do not present Neutral as a learned class or report a Neutral accuracy.
- Do not tune the threshold or models on the test set.
- Do not leave the notebook with errors, unused experiments, or hidden state.
- Do not use heavy deep-learning models or paid APIs. The student must be able to explain everything, so keep it classical ML.
- Do not copy huge, unexplained code blocks. Prefer short, clear functions.

**Optional extras (only after everything above is complete and tested)**
- Word2Vec or a small embedding comparison as a future-work demo.
- Bag of Words vs TF-IDF comparison table.
- Showing the most influential words (largest positive and negative Logistic Regression coefficients) in the app's About tab.

---

## 9. How to run (document this in the final `README.md`)

```bash
pip install -r requirements.txt
jupyter notebook                 # open sentiment_analysis.ipynb, Run All (creates artifacts/)
streamlit run app.py             # launches the GUI in the browser
pytest -v                        # runs the tests
```

The Streamlit app requires the notebook to have been run first (it needs `artifacts/`). **Ship the project with `artifacts/` already generated**, so the app works immediately.

---

## 10. Acceptance criteria per stage (checklist the agent must self-verify)

| Stage | Done when |
|---|---|
| 1 | Markdown cell explains problem, objective, applications, approach, Neutral decision |
| 2 | `train_df` / `test_df` loaded, shape and samples shown, dataset explained |
| 3 | Missing values, duplicates, empty rows, inconsistent ratings handled, before/after counts shown |
| 4 | `preprocess.py` implements all steps, negation kept, before/after examples, cleaned columns cached |
| 5 | At least 4 saved charts, each with a written observation |
| 6 | TF-IDF fitted on train split only, parameters explained, shape shown |
| 7 | 3 models compared in a table; Logistic Regression selected with reason |
| 8 | Test metrics + confusion matrix; threshold chosen on validation with evidence chart; 10+ sentence check; artifacts saved |
| 9 | Streamlit app has input box, button, Positive/Negative/Neutral result, confidence; handles empty/gibberish input |
| 10 | pytest passes; notebook executes cleanly; app smoke test passes; manual test table filled |

---

## 11. Additional deliverables to generate

1. **`README.md` (short, for submission):** project title, one-paragraph description, features, tech stack, folder structure, how to run, results summary (accuracy, F1), limitations. Use the **real numbers** from your run.
2. **`REPORT.md`:** a project report with the 10 stages as sections (Introduction/Problem, Dataset, Cleaning, Preprocessing, EDA, Feature Engineering, Models, Evaluation, GUI, Testing), plus Conclusion, Limitations and Future Work. Embed or reference the saved charts and tables. Plain language, suitable for a college report.
3. **`VIVA_QA.md`:** at least 25 likely viva questions with short, simple answers specific to **this** project. Must cover: what is sentiment analysis, why IMDb, how Neutral is handled, tokenization, stopwords and why negations are kept, stemming vs lemmatization, TF-IDF (TF, IDF, formula intuition), Bag of Words vs TF-IDF, n-grams, why Logistic Regression, how Naive Bayes and SVM work in one line, train/validation/test split, data leakage, precision/recall/F1/confusion matrix, why accuracy alone is not enough, confidence/probability, threshold choice, limitations (sarcasm, domain shift), how the app works end to end, why Streamlit, and future improvements (BERT, 3-class datasets).
4. **Presentation outline (inside `REPORT.md` or a separate `PRESENTATION_OUTLINE.md`):** 10-12 slides with bullet points per slide.

---

## 12. Definition of Done

The project is complete only when **all** of the following are true:

- [ ] `sentiment_analysis.ipynb` runs top to bottom without errors, covers Stages 1-8 and 10, and is saved with outputs.
- [ ] `artifacts/` contains `tfidf.joblib`, `model.joblib`, `config.json`, `metrics.json`.
- [ ] `streamlit run app.py` launches, and the app shows Positive, Negative and Neutral results with confidence for suitable inputs.
- [ ] Empty input and gibberish are handled without crashing.
- [ ] `pytest -v` passes (or any failures are explained honestly and not hidden).
- [ ] `outputs/` contains the EDA charts, model comparison table, classification report, confusion matrix and confidence-by-rating chart.
- [ ] `README.md`, `REPORT.md`, `VIVA_QA.md`, `requirements.txt` exist and use real results.
- [ ] No test-set leakage, negation words are preserved, and the Neutral limitation is stated clearly everywhere it matters.

---

## 13. Final message the agent should give to the student

When finished, summarise in simple language:
1. What was built and where each file is.
2. The actual results (test accuracy, precision, recall, F1, chosen threshold and why).
3. Anything that did not work perfectly (be honest).
4. The 3 commands to run the project.
5. The 5 most important concepts the student should revise before the viva.

If anything in this specification is ambiguous or impossible in your environment, choose the simplest option that still satisfies the faculty requirements in Section 2, and **state the assumption** in your final message.
