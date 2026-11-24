# 🎤 Presentation Speaker Notes & Viva Defense Script
## Movie Review Sentiment Analysis using NLP & Machine Learning

Use this script during your presentation and viva exam. It provides the exact talking points and explanations for each slide of `Movie_Sentiment_Analysis_Presentation.pptx`.

---

### Slide 1: Title Slide
> **What to say:**  
> "Good morning, respected faculty and classmates. Today, I am presenting our 5th-semester NLP project titled **'Movie Review Sentiment Analysis Using NLP and Machine Learning'**. In this project, we have built a complete, end-to-end sentiment classification system from scratch—spanning dataset auditing, linguistic preprocessing, feature engineering, model benchmarking, and an interactive web GUI using Streamlit."

---

### Slide 2: Introduction & Motivation
> **What to say:**  
> "Why is sentiment analysis important? In the entertainment industry, platforms like IMDb and social media receive millions of reviews. Manually reading through them to gauge public reception is virtually impossible. Sentiment analysis uses NLP to convert this raw, unstructured textual data into numerical vectors and classify the underlying opinion. This has direct real-world applications in box-office reception tracking, brand monitoring, and automated customer support."

---

### Slide 3: Problem Statement & Objectives
> **What to say:**  
> "Our objective was to build a reliable classifier that ingests movie reviews in plain English and predicts whether the review expresses positive or negative sentiment. We structured our development across the 10 academic engineering stages: ingesting 50,000 labelled reviews, engineering sublinear TF-IDF features with negation preservation, comparing multiple classification algorithms, and building a live web interface."

---

### Slide 4: Dataset Architecture (Stanford IMDb) & Scope Disclosure
> **What to say:**  
> "For our dataset, we used the Stanford Large Movie Review Dataset (`aclImdb`) created by Maas et al. It contains 50,000 reviews evenly divided into 25,000 training and 25,000 test reviews, with a perfectly balanced 50-50 class split.  
> **Important Note on Academic Scope:** While generic briefs mention positive, negative, and neutral classes, the Stanford IMDb dataset only contains highly polarized reviews—scores of 7 and above are positive, scores of 4 and below are negative. Neutral scores (5 and 6) were excluded by the Stanford researchers. Therefore, in line with academic integrity, our system is formulated strictly as a binary classifier rather than guessing artificial neutral labels."

---

### Slide 5: NLP Pipeline & Data Leakage Prevention
> **What to say:**  
> "Here is our complete system architecture. A user enters a review into our Streamlit GUI. The text is cleaned and preprocessed, transformed into numerical features using TF-IDF, and evaluated by our Linear SVM classifier to produce a prediction and confidence score.  
> Crucially, we guaranteed **Zero Data Leakage**. The TF-IDF vectorizer was fitted strictly on the training partition inside a `scikit-learn Pipeline`. The test set of 25,000 reviews remained untouched until final evaluation."

---

### Slide 6: Text Preprocessing & Negation Preservation
> **What to say:**  
> "Text preprocessing is not just about removing words. In sentiment analysis, standard stopword removal introduces a major flaw: it removes words like 'not', 'no', and 'never'.  
> If someone writes *'The movie was not good'*, standard stopword removal turns it into *'movie good'*, which completely reverses the meaning from negative to positive!  
> To solve this, we implemented a custom preprocessor that strips HTML and normalizes text while **strictly preserving all 26 English negation words**."

---

### Slide 7: Feature Engineering: BoW vs. TF-IDF
> **What to say:**  
> "We compared Bag of Words and TF-IDF. Bag of Words only counts word occurrences, so ubiquitous words like 'movie' or 'film' dominate the feature matrix. TF-IDF solves this by applying an Inverse Document Frequency penalty to common words while elevating distinctive sentiment signals like 'masterpiece' or 'terrible'.  
> We configured TF-IDF with unigrams and bigrams, sublinear term-frequency scaling, and a 100,000-feature vocabulary."

---

### Slide 8: Model Development & Validation Benchmarking
> **What to say:**  
> "We trained and compared three candidate algorithms on an 80/20 train/validation split:
> 1. **Multinomial Naive Bayes** achieved **88.06%** validation accuracy.
> 2. **Logistic Regression** achieved **88.92%** validation accuracy.
> 3. **Linear Support Vector Machine (LinearSVC)** achieved **90.00%** validation accuracy.  
> Linear SVM was selected because maximum-margin hyperplanes excel at separating high-dimensional, sparse text vectors."

---

### Slide 9: Held-Out Test Evaluation & Confusion Matrix
> **What to say:**  
> "We then evaluated our selected Linear SVM on the 25,000 unseen test reviews.  
> It achieved an overall **Test Accuracy of 89.90%** and a **Macro F1-score of 0.8990**.  
> The confusion matrix shows near-perfect balance: 11,247 true negatives and 11,227 true positives, confirming that our model generalizes well without overfitting."

---

### Slide 10: Streamlit GUI Demonstration
> **What to say:**  
> "In accordance with the faculty brief requiring a user-friendly GUI, we built an interactive web app with Streamlit. It includes:
> - 1-click sample review buttons for quick testing.
> - Clear visual sentiment badges with model confidence percentages.
> - A Linguistic Preprocessing tab that highlights preserved negation words.
> - Embedded confusion matrices and pipeline inspection tabs."

---

### Slide 11: Testing & Verification
> **What to say:**  
> "We subjected the system to edge-case testing: clear positive reviews, clear negative reviews, complex negation sentences like *'The film was not good and I did not enjoy it'*, and empty input. All test cases passed with high confidence."

---

### Slide 12: Limitations & Future Scope
> **What to say:**  
> "Our current limitations are the binary scope inherent to the IMDb dataset, domain specialization to movies, and subtle sarcasm. In the future, this can be expanded by fine-tuning transformer models like DistilBERT and incorporating the Stanford Sentiment Treebank (SST-3) for neutral-class classification."

---

### Slide 13 & 14: Conclusion & Viva Q&A
> **What to say:**  
> "To conclude, this project successfully demonstrates the entire NLP lifecycle from raw text to a deployed machine learning application achieving nearly 90% accuracy. Thank you, and I am now ready for your questions."
