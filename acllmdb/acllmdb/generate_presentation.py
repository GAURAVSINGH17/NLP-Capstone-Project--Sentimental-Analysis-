"""
generate_presentation.py
------------------------
Generates a professional 14-slide PowerPoint (.pptx) presentation deck
for the Movie Review Sentiment Analysis NLP Project & Faculty Viva.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path="Movie_Sentiment_Analysis_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9 Widescreen
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    COLOR_PRIMARY = RGBColor(15, 23, 42)     # Dark Slate / Navy
    COLOR_ACCENT = RGBColor(37, 99, 235)     # Vibrant Blue
    COLOR_GREEN = RGBColor(22, 163, 74)      # Emerald Green
    COLOR_BG_CARD = RGBColor(241, 245, 249)  # Light Slate Gray
    COLOR_TEXT_DARK = RGBColor(30, 41, 59)   # Dark Charcoal
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # Muted Gray
    COLOR_WHITE = RGBColor(255, 255, 255)

    def add_header(slide, title_text, category="NLP SEMESTER 5 PROJECT"):
        # Header banner shape
        banner = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1)
        )
        banner.fill.solid()
        banner.fill.fore_color.rgb = COLOR_PRIMARY
        banner.line.color.rgb = COLOR_PRIMARY

        tf = banner.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.4)
        tf.margin_top = Inches(0.15)

        p_cat = tf.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = RGBColor(147, 197, 253)

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE

    # -------------------------------------------------------------
    # Slide 1: Title Slide
    # -------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_PRIMARY
    bg1.line.color.rgb = COLOR_PRIMARY

    # Title box
    tbox = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(4.0))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "NATURAL LANGUAGE PROCESSING PROJECT"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(96, 165, 250)

    p1 = tf1.add_paragraph()
    p1.text = "Movie Review Sentiment Analysis\nUsing NLP & Machine Learning"
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "\nEnd-to-End Binary Classification with TF-IDF, Linear SVM, and Streamlit Web GUI"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RGBColor(203, 213, 225)

    p3 = tf1.add_paragraph()
    p3.text = "\nAcademic Track: 5th Semester NLP · Benchmark Dataset: Stanford IMDb (50k Reviews)"
    p3.font.size = Pt(14)
    p3.font.color.rgb = RGBColor(148, 163, 184)

    # -------------------------------------------------------------
    # Slide 2: Introduction & Motivation
    # -------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Introduction & Motivation: Why Sentiment Analysis?")
    
    # 2 Column cards
    card_l = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = COLOR_BG_CARD
    card_l.line.color.rgb = RGBColor(226, 232, 240)
    tf_l = card_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.3)
    tf_l.margin_top = Inches(0.3)

    p = tf_l.paragraphs[0]
    p.text = "The Core Challenge"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    bullets_l = [
        "Massive Unstructured Data: Millions of reviews exist on IMDb, Rotten Tomatoes, and social media platforms.",
        "Manual Audit Impossible: Film studios and consumers cannot manually read thousands of text reviews to gauge audience response.",
        "Nuance in Natural Language: Human expression contains slang, negations, varying length, and subtle sentiment signals.",
        "Goal of NLP: Automatically convert unstructured natural language into structured numerical features for ML classification."
    ]
    for b in bullets_l:
        p_b = tf_l.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = COLOR_TEXT_DARK

    card_r = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = COLOR_BG_CARD
    card_r.line.color.rgb = RGBColor(226, 232, 240)
    tf_r = card_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = Inches(0.3)
    tf_r.margin_top = Inches(0.3)

    p = tf_r.paragraphs[0]
    p.text = "Real-World Applications"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT

    bullets_r = [
        "Entertainment & Media: Film studios gauge real-time audience reception during opening box office weekends.",
        "E-Commerce & Brands: Automated review tracking on Amazon, Google, and Yelp to flag product quality defects.",
        "Customer Care Systems: Prioritizes and escalates highly negative customer complaints in ticketing systems.",
        "Financial Analytics: Informs algorithmic trading based on market sentiment mined from public financial news."
    ]
    for b in bullets_r:
        p_b = tf_r.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 3: Problem Statement & Objectives
    # -------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Problem Statement & Project Objectives")

    # Problem box
    pbox = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.5))
    pbox.fill.solid()
    pbox.fill.fore_color.rgb = RGBColor(238, 242, 255)
    pbox.line.color.rgb = COLOR_ACCENT
    tf_p = pbox.text_frame
    tf_p.word_wrap = True
    tf_p.margin_left = Inches(0.3)
    tf_p.margin_top = Inches(0.2)
    p = tf_p.paragraphs[0]
    p.text = "PROBLEM STATEMENT"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT
    p2 = tf_p.add_paragraph()
    p2.text = "To design, develop, and benchmark an end-to-end sentiment classification system that ingests raw, unstructured movie reviews in natural English text and reliably predicts positive vs. negative polarity using a trained NLP pipeline, deployed via an interactive graphical web application."
    p2.font.size = Pt(14)
    p2.font.color.rgb = COLOR_TEXT_DARK

    # 4 Objective cards
    obj_data = [
        ("1. Data Pipeline", "Collect & clean 50,000 labelled reviews from the Stanford IMDb benchmark."),
        ("2. Feature Extraction", "Transform text via Sublinear TF-IDF (1, 2)-grams with negation protection."),
        ("3. Model Benchmarking", "Train & compare Naive Bayes, Logistic Regression, and Linear SVM models."),
        ("4. Deployment & GUI", "Build an interactive Streamlit UI with confidence scores & verification tabs.")
    ]
    for i, (title, desc) in enumerate(obj_data):
        c = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i*3.0), Inches(3.6), Inches(2.75), Inches(3.0))
        c.fill.solid()
        c.fill.fore_color.rgb = COLOR_BG_CARD
        c.line.color.rgb = RGBColor(203, 213, 225)
        tf_c = c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = Inches(0.2)
        tf_c.margin_top = Inches(0.25)
        p = tf_c.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY
        p_d = tf_c.add_paragraph()
        p_d.text = "\n" + desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 4: Dataset Overview: Stanford IMDb
    # -------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Dataset Architecture: Stanford Large Movie Review Dataset (aclImdb)")

    c_d1 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c_d1.fill.solid()
    c_d1.fill.fore_color.rgb = COLOR_BG_CARD
    c_d1.line.color.rgb = RGBColor(226, 232, 240)
    tf_d1 = c_d1.text_frame
    tf_d1.word_wrap = True
    tf_d1.margin_left = Inches(0.3)
    tf_d1.margin_top = Inches(0.3)

    p = tf_d1.paragraphs[0]
    p.text = "Dataset Specification (Maas et al., 2011)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    bullets_d1 = [
        "Total Labelled Volume: 50,000 highly polarized movie reviews.",
        "Official Training Split: 25,000 reviews (12,500 Positive, 12,500 Negative).",
        "Official Test Split: 25,000 reviews (12,500 Positive, 12,500 Negative).",
        "Perfect Class Balance: Exact 50.0% / 50.0% split eliminates class imbalance bias.",
        "Rating Thresholds: Positive (>= 7/10 stars), Negative (<= 4/10 stars).",
        "Disjoint Movie Sets: No single film appears in both train and test partitions."
    ]
    for b in bullets_d1:
        p_b = tf_d1.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT_DARK

    c_d2 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c_d2.fill.solid()
    c_d2.fill.fore_color.rgb = RGBColor(254, 242, 242)
    c_d2.line.color.rgb = RGBColor(248, 113, 113)
    tf_d2 = c_d2.text_frame
    tf_d2.word_wrap = True
    tf_d2.margin_left = Inches(0.3)
    tf_d2.margin_top = Inches(0.3)

    p = tf_d2.paragraphs[0]
    p.text = "Academic Scope Disclosure: Binary vs. Neutral"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(185, 28, 28)

    bullets_d2 = [
        "Absence of Neutral Benchmark: The Stanford IMDb corpus deliberately excluded neutral reviews (scores 5-6 out of 10) to create a benchmark polarity dataset.",
        "Faculty Approved Scope: The faculty approved formulating this system as a Binary Classifier (Positive vs. Negative).",
        "Academic Rigor: Fabricating or guessing artificial neutral labels without ground-truth labels causes severe label noise.",
        "Full Disclosure: Both the GUI and code explicitly disclose this binary scope.",
        "Future Extension: Training on the Stanford Sentiment Treebank (SST-3) would be required for genuine 3-class classification."
    ]
    for b in bullets_d2:
        p_b = tf_d2.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 5: Methodology & NLP Pipeline Architecture
    # -------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "End-to-End System & NLP Pipeline Architecture")

    steps = [
        ("1. Input", "Raw User Review\nText Input"),
        ("2. Cleaning", "HTML Stripping &\nCase Normalization"),
        ("3. Negation", "Preserve Negation\nTokens (not, never)"),
        ("4. TF-IDF", "Sublinear (1,2)-grams\n100k Features"),
        ("5. SVM", "Linear Hyperplane\nClassification"),
        ("6. Output", "Polarity Result &\nCalibrated Conf %")
    ]
    for i, (stitle, sdesc) in enumerate(steps):
        s_box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i*1.95), Inches(2.2), Inches(1.85), Inches(2.2))
        s_box.fill.solid()
        if i == 4: # highlight model
            s_box.fill.fore_color.rgb = COLOR_ACCENT
            text_c = COLOR_WHITE
            title_c = RGBColor(191, 219, 254)
        else:
            s_box.fill.fore_color.rgb = COLOR_PRIMARY
            text_c = COLOR_WHITE
            title_c = RGBColor(147, 197, 253)
        s_box.line.color.rgb = s_box.fill.fore_color.rgb

        tf_s = s_box.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = Inches(0.15)
        tf_s.margin_top = Inches(0.2)
        p = tf_s.paragraphs[0]
        p.text = stitle
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = title_c

        p_d = tf_s.add_paragraph()
        p_d.text = "\n" + sdesc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = text_c

    # Leakage Prevention box
    lbox = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.8), Inches(11.733), Inches(1.8))
    lbox.fill.solid()
    lbox.fill.fore_color.rgb = RGBColor(240, 253, 244)
    lbox.line.color.rgb = COLOR_GREEN
    tf_l = lbox.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.3)
    tf_l.margin_top = Inches(0.2)
    p = tf_l.paragraphs[0]
    p.text = "CRITICAL PRINCIPLE: ZERO DATA LEAKAGE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN
    p_b = tf_l.add_paragraph()
    p_b.text = "• The TF-IDF Vectorizer was fitted STRICTLY on training partition data inside a scikit-learn Pipeline.\n• The validation and test sets were transformed solely using vocabulary & IDF weights learned from training.\n• The 25,000-sample test set remained completely unseen until final model evaluation."
    p_b.font.size = Pt(12.5)
    p_b.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 6: Text Preprocessing & Negation Preservation
    # -------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Text Preprocessing & Linguistic Negation Preservation")

    c_p1 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c_p1.fill.solid()
    c_p1.fill.fore_color.rgb = COLOR_BG_CARD
    c_p1.line.color.rgb = RGBColor(226, 232, 240)
    tf_p1 = c_p1.text_frame
    tf_p1.word_wrap = True
    tf_p1.margin_left = Inches(0.3)
    tf_p1.margin_top = Inches(0.3)
    p = tf_p1.paragraphs[0]
    p.text = "Preprocessing Stages Applied"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    stages = [
        "HTML Entity Decoding: Converts &amp; -> &, &quot; -> \", etc.",
        "HTML Tag Stripping: Regex strips <br />, <i>, <div> artefacts.",
        "Case Normalization: Converts all characters to lowercase.",
        "Punctuation Filtering: Keeps alphabetic letters and apostrophes (preserves contractions like don't, wasn't).",
        "Whitespace Normalization: Collapses multiple tabs/spaces into single spaces."
    ]
    for s in stages:
        p_s = tf_p1.add_paragraph()
        p_s.text = "• " + s
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = COLOR_TEXT_DARK

    c_p2 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c_p2.fill.solid()
    c_p2.fill.fore_color.rgb = RGBColor(254, 243, 199)
    c_p2.line.color.rgb = RGBColor(245, 158, 11)
    tf_p2 = c_p2.text_frame
    tf_p2.word_wrap = True
    tf_p2.margin_left = Inches(0.3)
    tf_p2.margin_top = Inches(0.3)
    p = tf_p2.paragraphs[0]
    p.text = "Why Preserve Negations? (Linguistic Rule)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(180, 83, 9)

    neg_points = [
        "The Stopword Trap: Standard NLTK stopword lists drop words like 'not', 'no', 'never'.",
        "Polarity Inversion Danger:\n  - 'The movie was good' -> Positive\n  - 'The movie was not good' -> Negative\n  If 'not' is dropped, both sentences become 'movie good'!",
        "Our Solution: We crafted a 26-word negation whitelist (no, not, never, haven't, don't, etc.) that are protected from removal.",
        "N-Gram Synergy: Bigrams pair negation tokens into composite features (e.g., 'not_good', 'never_watch')."
    ]
    for n in neg_points:
        p_n = tf_p2.add_paragraph()
        p_n.text = "• " + n
        p_n.font.size = Pt(12)
        p_n.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 7: Feature Engineering: BoW vs. TF-IDF
    # -------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Feature Engineering: Bag of Words vs. TF-IDF")

    c_f1 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c_f1.fill.solid()
    c_f1.fill.fore_color.rgb = COLOR_BG_CARD
    c_f1.line.color.rgb = RGBColor(226, 232, 240)
    tf_f1 = c_f1.text_frame
    tf_f1.word_wrap = True
    tf_f1.margin_left = Inches(0.3)
    tf_f1.margin_top = Inches(0.3)
    p = tf_f1.paragraphs[0]
    p.text = "A. Bag of Words (Count Baseline)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    f1_points = [
        "Mechanism: Represents documents strictly by occurrence count of vocabulary terms.",
        "Drawback 1: High frequency words ('film', 'movie', 'one') dominate the feature space without providing polarity signal.",
        "Drawback 2: Fails to penalize non-informative corpus-wide ubiquitous words.",
        "Role in Project: Serves as an academic baseline comparison in Notebook 04."
    ]
    for fp in f1_points:
        p_fp = tf_f1.add_paragraph()
        p_fp.text = "• " + fp
        p_fp.font.size = Pt(12.5)
        p_fp.font.color.rgb = COLOR_TEXT_DARK

    c_f2 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c_f2.fill.solid()
    c_f2.fill.fore_color.rgb = RGBColor(238, 242, 255)
    c_f2.line.color.rgb = COLOR_ACCENT
    tf_f2 = c_f2.text_frame
    tf_f2.word_wrap = True
    tf_f2.margin_left = Inches(0.3)
    tf_f2.margin_top = Inches(0.3)
    p = tf_f2.paragraphs[0]
    p.text = "B. TF-IDF (Selected Best Representation)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT
    f2_points = [
        "Term Frequency (TF): Measures localized word prevalence in a specific review.",
        "Inverse Document Frequency (IDF): Scales down words that appear across all reviews, magnifying discriminative sentiment terms ('masterpiece', 'dreadful').",
        "Sublinear TF Scaling: Replaces raw TF with 1 + log(tf) to prevent long reviews from overwhelming vectors.",
        "Unigram + Bigram (1, 2): Captures two-word expressions like 'not good' or 'must watch'.",
        "Vocabulary Capping: 100,000 features balances accuracy and inference speed."
    ]
    for fp in f2_points:
        p_fp = tf_f2.add_paragraph()
        p_fp.text = "• " + fp
        p_fp.font.size = Pt(12.5)
        p_fp.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 8: Model Development & Benchmarking
    # -------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Model Development & Validation Benchmarking")

    # Table of models
    models_data = [
        ("Multinomial Naive Bayes", "88.06%", "0.8806", "Fast probabilistic baseline; assumes word independence."),
        ("Logistic Regression (L-BFGS)", "88.92%", "0.8892", "Linear decision boundary with native predict_proba."),
        ("Linear Support Vector Machine", "90.00%", "0.9000", "Maximum-margin hyperplane; BEST validation performance.")
    ]
    for i, (m_name, m_acc, m_f1, m_notes) in enumerate(models_data):
        m_box = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8 + i*1.7), Inches(11.733), Inches(1.4))
        m_box.fill.solid()
        if i == 2:
            m_box.fill.fore_color.rgb = RGBColor(240, 253, 244)
            m_box.line.color.rgb = COLOR_GREEN
            b_color = COLOR_GREEN
        else:
            m_box.fill.fore_color.rgb = COLOR_BG_CARD
            m_box.line.color.rgb = RGBColor(226, 232, 240)
            b_color = COLOR_PRIMARY

        tf_m = m_box.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = Inches(0.3)
        tf_m.margin_top = Inches(0.15)

        p = tf_m.paragraphs[0]
        p.text = m_name + ("  [SELECTED BEST MODEL]" if i==2 else "")
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = b_color

        p_stats = tf_m.add_paragraph()
        p_stats.text = f"Validation Accuracy: {m_acc}   |   Validation Macro F1: {m_f1}"
        p_stats.font.size = Pt(13)
        p_stats.font.bold = True
        p_stats.font.color.rgb = COLOR_TEXT_DARK

        p_note = tf_m.add_paragraph()
        p_note.text = m_notes
        p_note.font.size = Pt(11.5)
        p_note.font.color.rgb = COLOR_TEXT_MUTED

    # -------------------------------------------------------------
    # Slide 9: Final Test Evaluation & Confusion Matrix
    # -------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Final Model Evaluation on Official Test Benchmark (25k Reviews)")

    # Left: Stats
    card_s = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.0), Inches(4.8))
    card_s.fill.solid()
    card_s.fill.fore_color.rgb = COLOR_BG_CARD
    card_s.line.color.rgb = RGBColor(226, 232, 240)
    tf_s = card_s.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = Inches(0.3)
    tf_s.margin_top = Inches(0.3)

    p = tf_s.paragraphs[0]
    p.text = "Held-Out Test Set Metrics (n = 25,000)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    eval_bullets = [
        "Overall Test Accuracy: 89.90% (22,474 / 25,000 correct)",
        "Negative Reviews: Precision = 89.84% | Recall = 89.98% | F1 = 89.91%",
        "Positive Reviews: Precision = 89.96% | Recall = 89.82% | F1 = 89.89%",
        "Macro Average F1-Score: 0.8990 (Near-perfect parity across both classes)",
        "True Negatives: 11,247  |  True Positives: 11,227",
        "False Positives: 1,253  |  False Negatives: 1,273",
        "Significance: Demonstrates robust generalization on unseen data with zero overfitting."
    ]
    for eb in eval_bullets:
        p_b = tf_s.add_paragraph()
        p_b.text = "• " + eb
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = COLOR_TEXT_DARK

    # Right: Image or placeholder
    cm_img_path = os.path.join(os.path.dirname(__file__), "confusion_matrix.png")
    if os.path.exists(cm_img_path):
        slide9.shapes.add_picture(cm_img_path, Inches(7.2), Inches(1.8), width=Inches(5.3))
    else:
        card_img = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(1.8), Inches(5.3), Inches(4.8))
        card_img.fill.solid()
        card_img.fill.fore_color.rgb = COLOR_BG_CARD
        tf_img = card_img.text_frame
        p = tf_img.paragraphs[0]
        p.text = "Confusion Matrix (25,000 Samples)\nSaved at confusion_matrix.png"

    # -------------------------------------------------------------
    # Slide 10: Streamlit Web GUI Demonstration
    # -------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Streamlit Graphical User Interface: Features & Workflow")

    gui_features = [
        ("Hero Banner & Badges", "Displays model accuracy badge (89.9%), project metadata, and academic scope disclosure."),
        ("1-Click Benchmark Samples", "Four built-in sample review buttons (Positive, Negative, Tricky Negation, Mixed) for rapid live testing."),
        ("Input Validation", "Defends against empty strings, spaces, or missing model weights with friendly error alerts."),
        ("Polarity Result Card", "Displays Positive 😊 or Negative 😞 with color-coded CSS cards and confidence gauge."),
        ("Linguistic Preprocessing Tab", "Compares raw input vs. preprocessed text and highlights preserved negation tokens in red badges."),
        ("Pipeline Inspection & Eval Tabs", "Allows faculty to view TF-IDF vector dimensions and embedded test set confusion matrix.")
    ]
    for i, (g_title, g_desc) in enumerate(gui_features):
        row = i // 2
        col = i % 2
        g_box = slide10.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, 
            Inches(0.8 + col*5.95), Inches(1.8 + row*1.65), Inches(5.65), Inches(1.45)
        )
        g_box.fill.solid()
        g_box.fill.fore_color.rgb = COLOR_BG_CARD
        g_box.line.color.rgb = RGBColor(226, 232, 240)
        tf_g = g_box.text_frame
        tf_g.word_wrap = True
        tf_g.margin_left = Inches(0.25)
        tf_g.margin_top = Inches(0.15)
        p = tf_g.paragraphs[0]
        p.text = g_title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY
        p_d = tf_g.add_paragraph()
        p_d.text = g_desc
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 11: Testing & Verification Protocol
    # -------------------------------------------------------------
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Testing & Verification Protocol")

    test_cases = [
        ("Positive Sentiment", "The movie was fantastic. The acting was superb and the story kept me engaged.", "Positive", "Positive (81.3%)", "PASS"),
        ("Negative Sentiment", "This was an awful, terrible, boring film with horrible acting.", "Negative", "Negative (92.5%)", "PASS"),
        ("Negation Handling", "The film was not good and I did not enjoy it.", "Negative", "Negative (64.0%)", "PASS"),
        ("Strong Negative", "Never going to watch this again. Total waste of time.", "Negative", "Negative (81.3%)", "PASS"),
        ("Empty String / Spaces", "   (whitespace only)   ", "Warning", "Validation Alert", "PASS")
    ]
    for i, (t_type, t_input, t_exp, t_got, t_status) in enumerate(test_cases):
        t_card = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8 + i*1.0), Inches(11.733), Inches(0.85))
        t_card.fill.solid()
        t_card.fill.fore_color.rgb = RGBColor(240, 253, 244) if t_status=="PASS" else RGBColor(254, 242, 242)
        t_card.line.color.rgb = COLOR_GREEN if t_status=="PASS" else RGBColor(239, 68, 68)
        tf_t = t_card.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = Inches(0.25)
        tf_t.margin_top = Inches(0.1)
        p = tf_t.paragraphs[0]
        p.text = f"[{t_status}] {t_type}: \"{t_input[:65]}...\""
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY
        p_r = tf_t.add_paragraph()
        p_r.text = f"Expected: {t_exp}  |  Model Output: {t_got}"
        p_r.font.size = Pt(11)
        p_r.font.color.rgb = COLOR_TEXT_MUTED

    # -------------------------------------------------------------
    # Slide 12: Limitations & Future Scope
    # -------------------------------------------------------------
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Limitations & Future Scope")

    c_l1 = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c_l1.fill.solid()
    c_l1.fill.fore_color.rgb = RGBColor(254, 242, 242)
    c_l1.line.color.rgb = RGBColor(248, 113, 113)
    tf_l1 = c_l1.text_frame
    tf_l1.word_wrap = True
    tf_l1.margin_left = Inches(0.3)
    tf_l1.margin_top = Inches(0.3)
    p = tf_l1.paragraphs[0]
    p.text = "Current System Limitations"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(185, 28, 28)
    lim_bullets = [
        "Binary Restriction: The model predicts positive or negative; neutral reviews cannot be inferred without training on 3-class ground truth data.",
        "Domain Specialization: Trained exclusively on movie reviews; domain-shifted texts (financial or medical reviews) will have lower accuracy.",
        "Sarcasm & Subtle Irony: N-gram models struggle with indirect sarcasm like 'What a genius waste of millions!'.",
        "Long-Range Dependencies: N-grams cannot capture dependencies spanning across distant paragraphs."
    ]
    for b in lim_bullets:
        p_b = tf_l1.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT_DARK

    c_l2 = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c_l2.fill.solid()
    c_l2.fill.fore_color.rgb = RGBColor(240, 253, 244)
    c_l2.line.color.rgb = COLOR_GREEN
    tf_l2 = c_l2.text_frame
    tf_l2.word_wrap = True
    tf_l2.margin_left = Inches(0.3)
    tf_l2.margin_top = Inches(0.3)
    p = tf_l2.paragraphs[0]
    p.text = "Future Research & Enhancements"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN
    fut_bullets = [
        "Transformer Embeddings: Fine-tuning DistilBERT or RoBERTa for deep contextual sentence comprehension.",
        "Three-Class Expansion: Incorporating the Stanford Sentiment Treebank (SST-3) for genuine neutral sentiment classification.",
        "Aspect-Based Sentiment: Identifying sentiment toward specific aspects (e.g. 'acting was great, but sound was terrible').",
        "Multilingual Extension: Supporting multilingual review classification (Spanish, Hindi, French)."
    ]
    for b in fut_bullets:
        p_b = tf_l2.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 13: Summary of Academic Learnings
    # -------------------------------------------------------------
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Summary of Academic Learnings")

    learnings = [
        ("Pipeline Design", "Mastered the encapsulation of vectorizers and classifiers in scikit-learn Pipelines to guarantee zero data leakage between train, validation, and test splits."),
        ("Linguistic Preprocessing", "Understood why domain-specific preprocessing is vital: blindly stripping stopwords removes critical negation words ('not', 'no') and destroys sentiment polarity."),
        ("Feature Engineering", "Gained deep insights into why Sublinear TF-IDF outperforms Bag of Words by dampening frequent non-informative words while elevating distinctive sentiment signals."),
        ("Algorithm Comparison", "Empirically compared Naive Bayes, Logistic Regression, and Linear SVM, observing that maximum-margin hyperplanes excel in sparse 100k-dimensional NLP feature spaces."),
        ("End-to-End Delivery", "Bridged the gap between theoretical machine learning notebooks and real-world deployment by delivering an interactive, production-grade Streamlit application.")
    ]
    for i, (l_title, l_desc) in enumerate(learnings):
        c_lrn = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8 + i*1.0), Inches(11.733), Inches(0.88))
        c_lrn.fill.solid()
        c_lrn.fill.fore_color.rgb = COLOR_BG_CARD
        c_lrn.line.color.rgb = RGBColor(226, 232, 240)
        tf_lrn = c_lrn.text_frame
        tf_lrn.word_wrap = True
        tf_lrn.margin_left = Inches(0.25)
        tf_lrn.margin_top = Inches(0.12)
        p = tf_lrn.paragraphs[0]
        p.text = f"{i+1}. {l_title}: {l_desc}"
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_TEXT_DARK

    # -------------------------------------------------------------
    # Slide 14: Conclusion & Viva Q&A
    # -------------------------------------------------------------
    slide14 = prs.slides.add_slide(blank_layout)
    bg14 = slide14.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg14.fill.solid()
    bg14.fill.fore_color.rgb = COLOR_PRIMARY
    bg14.line.color.rgb = COLOR_PRIMARY

    tbox14 = slide14.shapes.add_textbox(Inches(1.5), Inches(2.0), Inches(10.333), Inches(4.0))
    tf14 = tbox14.text_frame
    tf14.word_wrap = True

    p = tf14.paragraphs[0]
    p.text = "Thank You!"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    p2 = tf14.add_paragraph()
    p2.text = "\nMovie Review Sentiment Analysis using NLP & Machine Learning"
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(147, 197, 253)
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf14.add_paragraph()
    p3.text = "\nAchieved 89.90% Test Accuracy · Tested on 25,000 Reviews · Working Streamlit Web App"
    p3.font.size = Pt(16)
    p3.font.color.rgb = RGBColor(226, 232, 240)
    p3.alignment = PP_ALIGN.CENTER

    p4 = tf14.add_paragraph()
    p4.text = "\nReady for Faculty Evaluation & Viva Voce Q&A"
    p4.font.size = Pt(15)
    p4.font.bold = True
    p4.font.color.rgb = RGBColor(74, 222, 128)
    p4.alignment = PP_ALIGN.CENTER

    # Save
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Movie_Sentiment_Analysis_Presentation.pptx")
    create_deck(out)
