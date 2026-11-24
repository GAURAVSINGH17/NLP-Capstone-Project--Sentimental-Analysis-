# 🎤 Presentation Speaker Notes & Viva Defense Script
## Movie Review Sentiment Analysis using NLP & Machine Learning

Use this script during your presentation and viva exam. It maps directly to the 10 required sections in your updated **`Movie_Sentiment_Analysis_Presentation.pptx`**.

---

### Slide 1: Project Title and Team Members
> **What to say:**  
> "Good morning, respected faculty and classmates. Today, we are presenting our 5th-semester NLP project titled **'Movie Review Sentiment Analysis Using NLP and Machine Learning'**.  
> Our team members are [Your Name] and [Partner's Name]. Under the guidance of [Professor's Name], we built an end-to-end sentiment classification system from scratch—from raw text ingestion and linguistic preprocessing to feature engineering, model benchmarking, and an interactive web GUI using Streamlit."

---

### Slide 2: Problem Statement and Objectives
> **What to say:**  
> "Our problem statement was to design and deploy a complete NLP system that ingests unstructured natural language reviews, eliminates linguistic noise while preserving critical sentiment-reversing negations, extracts discriminative n-gram features, and reliably predicts positive vs. negative sentiment.  
> Our four core objectives were:
> 1. Ingest and validate 50,000 labelled reviews from the Stanford IMDb benchmark.
> 2. Transform text via Sublinear TF-IDF (1, 2)-grams with negation protection.
> 3. Train and compare Multinomial Naive Bayes, Logistic Regression, and Linear SVM.
> 4. Deploy a responsive Streamlit web application with real-time confidence scores."

---

### Slide 3: Introduction and Real-World Applications
> **What to say:**  
> "Sentiment analysis, or opinion mining, is the computational study of sentiments and emotions in text. In the entertainment industry, platforms like IMDb receive millions of reviews. Manual auditing is impossible. NLP bridges human expression and machine learning by transforming arbitrary text into normalized feature vectors.  
> Real-world applications include:
> - Box-office reception tracking for film studios.
> - Automated defect detection on e-commerce platforms like Amazon and Yelp.
> - Prioritization of urgent negative complaints in customer support ticketing systems."

---

### Slide 4: Dataset Description & Scope Disclosure
> **What to say:**  
> "We used the Stanford Large Movie Review Dataset (`aclImdb`) created by Maas et al. It contains 50,000 reviews evenly divided into 25,000 training and 25,000 test reviews, with a perfectly balanced 50-50 class split. Reviews with 7 or more stars are positive; reviews with 4 or fewer stars are negative.  
> **Academic Scope Note:** As approved by our faculty, this system is formulated as a binary classifier. The Stanford benchmark deliberately excluded neutral reviews (scores 5 and 6) to create a clean polarity benchmark. Fabricating an artificial neutral label without ground truth would introduce severe label noise. We transparently disclose this in our GUI and documentation."

---

### Slide 5: Data Preprocessing and EDA
> **What to say:**  
> "In data cleaning, we audited the dataset and confirmed zero missing values, zero empty documents, and 100% clean UTF-8 text records.  
> In text preprocessing, we stripped HTML tags and normalized casing.  
> **Crucial Linguistic Rule:** Standard stopword removal removes words like 'not', 'no', and 'never'. If someone writes *'The movie was not good'*, standard stopword removal turns it into *'movie good'*, which completely flips the meaning! We engineered a 26-word negation whitelist to strictly preserve negation words."

---

### Slide 6: Feature Engineering and Methodology
> **What to say:**  
> "We compared Bag of Words and TF-IDF. Bag of Words only counts frequencies, so generic words like 'movie' or 'film' dominate the matrix. TF-IDF applies an Inverse Document Frequency penalty to common words while elevating distinctive sentiment signals like 'masterpiece' or 'terrible'.  
> We configured TF-IDF with:
> - Sublinear TF scaling: $1 + \log(\text{tf})$ to dampen repetitive terms.
> - (1, 2)-grams: to capture phrases like 'not good' and 'must watch'.
> - **Zero Data Leakage:** The vectorizer was fitted strictly on the training partition inside a scikit-learn Pipeline; the test set was only transformed."

---

### Slide 7: Model Architecture and Algorithms
> **What to say:**  
> "We benchmarked three classification algorithms on an 80/20 train/validation split:
> 1. **Multinomial Naive Bayes** achieved **88.06%** validation accuracy. Fast, but its independence assumption limits performance on correlated n-grams.
> 2. **Logistic Regression** achieved **88.92%** validation accuracy. Strong linear baseline with native probability support.
> 3. **Linear Support Vector Machine (LinearSVC)** achieved **90.00%** validation accuracy. Linear SVM was selected because maximum-margin hyperplanes excel at separating ultra-high dimensional, sparse text vectors."

---

### Slide 8: Performance Evaluation and Results
> **What to say:**  
> "We evaluated the winning Linear SVM model on the untouched 25,000 held-out test reviews.  
> - **Overall Test Accuracy:** **89.90%** (22,474 out of 25,000 correct).  
> - **Macro F1-Score:** **0.8990**.  
> As shown on the slide in our confusion matrix: 11,247 true negatives and 11,227 true positives, confirming near-perfect balance and zero overfitting."

---

### Slide 9: GUI Screenshots and Working Demonstration
> **What to say:**  
> "To satisfy the mandatory GUI requirement, we built an interactive web app with Streamlit:
> - **1-Click Sample Reviews:** Quick buttons for positive, negative, tricky negation, and mixed reviews.
> - **Dynamic Polarity Card:** Displays clear green/red sentiment badges and confidence percentages.
> - **Linguistic Preprocessing Tab:** Compares raw vs cleaned text and visually flags preserved negation tokens.
> - **Evaluation Tab:** Directly embeds the confusion matrix inside the web app for faculty inspection."

---

### Slide 10: Conclusion and Future Scope
> **What to say:**  
> "In conclusion, we successfully built all 10 academic development stages from scratch, achieving 89.90% test accuracy and delivering a deployed web app.  
> For future work, we can explore:
> - Contextual transformers like DistilBERT or RoBERTa.
> - Incorporating the Stanford Sentiment Treebank (SST-3) for 3-class neutral sentiment classification.
> - Aspect-based sentiment analysis to evaluate specific movie dimensions like acting, plot, and cinematography."

---

### Slide 11: Viva Voce & Q&A
> **What to say:**  
> "Thank you for your time and attention. We are now open to any questions from the faculty."
