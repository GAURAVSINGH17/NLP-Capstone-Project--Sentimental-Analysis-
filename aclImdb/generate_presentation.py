"""
generate_presentation.py
------------------------
Generates a professional widescreen (16:9) PowerPoint presentation (.pptx)
strictly adhering to the faculty's required 10-point syllabus structure:

1. Project Title and Team Members
2. Problem Statement and Objectives
3. Introduction and Real-World Applications
4. Dataset Description
5. Data Preprocessing and EDA
6. Feature Engineering and Methodology
7. Model Architecture and Algorithms
8. Performance Evaluation and Results (with embedded confusion matrix)
9. GUI Screenshots and Working Demonstration (with embedded GUI showcase)
10. Conclusion and Future Scope
+ Bonus Slide 11: Viva Voce & Faculty Defense Cheat Sheet
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_path="Movie_Sentiment_Analysis_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9 Widescreen
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Professional Theme Palette
    COLOR_NAVY = RGBColor(15, 23, 42)        # Slate 900
    COLOR_BLUE = RGBColor(37, 99, 235)       # Blue 600
    COLOR_GREEN = RGBColor(22, 163, 74)      # Emerald 600
    COLOR_CARD = RGBColor(241, 245, 249)     # Slate 100
    COLOR_BORDER = RGBColor(226, 232, 240)   # Slate 200
    COLOR_TEXT = RGBColor(30, 41, 59)        # Slate 800
    COLOR_MUTED = RGBColor(100, 116, 139)    # Slate 500
    COLOR_WHITE = RGBColor(255, 255, 255)

    base_dir = os.path.dirname(os.path.abspath(__file__))

    def add_slide_header(slide, slide_num, title_text):
        banner = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1)
        )
        banner.fill.solid()
        banner.fill.fore_color.rgb = COLOR_NAVY
        banner.line.color.rgb = COLOR_NAVY

        tf = banner.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.4)
        tf.margin_top = Inches(0.15)

        p_sub = tf.paragraphs[0]
        p_sub.text = f"SECTION {slide_num} · 5TH SEMESTER NLP PROJECT"
        p_sub.font.size = Pt(11)
        p_sub.font.bold = True
        p_sub.font.color.rgb = RGBColor(147, 197, 253)

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE

    # =========================================================================
    # SLIDE 1: Project Title & Team Members
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = COLOR_NAVY
    bg1.line.color.rgb = COLOR_NAVY

    # Title Card
    tbox = s1.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.733), Inches(2.8))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING · NLP LAB"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(96, 165, 250)

    p1 = tf1.add_paragraph()
    p1.text = "Movie Review Sentiment Analysis\nUsing NLP & Machine Learning"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "A Complete End-to-End System: Data Preprocessing, TF-IDF, Linear SVM & Streamlit GUI"
    p2.font.size = Pt(17)
    p2.font.color.rgb = RGBColor(203, 213, 225)

    # Team Members Box (Left)
    card_tm = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.4))
    card_tm.fill.solid()
    card_tm.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_tm.line.color.rgb = RGBColor(51, 65, 85)
    tf_tm = card_tm.text_frame
    tf_tm.margin_left = Inches(0.3)
    tf_tm.margin_top = Inches(0.25)
    p = tf_tm.paragraphs[0]
    p.text = "👥 Project Team Members"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(147, 197, 253)

    members = [
        "1. [Student Name 1] — Roll No: [Your Roll No]",
        "2. [Student Name 2] — Roll No: [Partner Roll No] (if group)",
        "Class: 5th Semester B.Tech / BE (CSE)",
    ]
    for m in members:
        pm = tf_tm.add_paragraph()
        pm.text = m
        pm.font.size = Pt(13)
        pm.font.color.rgb = COLOR_WHITE

    # Academic & Guide Info (Right)
    card_gd = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.4))
    card_gd.fill.solid()
    card_gd.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card_gd.line.color.rgb = RGBColor(51, 65, 85)
    tf_gd = card_gd.text_frame
    tf_gd.margin_left = Inches(0.3)
    tf_gd.margin_top = Inches(0.25)
    p = tf_gd.paragraphs[0]
    p.text = "🏛️ Academic & Mentorship Details"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(74, 222, 128)

    guides = [
        "Project Guide: [Faculty / Professor Name]",
        "Course: Natural Language Processing (NLP)",
        "Benchmark Dataset: Stanford IMDb (50,000 Reviews)",
        "System Status: Tested & Deployed on Localhost (Streamlit)",
    ]
    for g in guides:
        pg = tf_gd.add_paragraph()
        pg.text = g
        pg.font.size = Pt(13)
        pg.font.color.rgb = COLOR_WHITE

    # =========================================================================
    # SLIDE 2: Problem Statement & Objectives
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "02", "Problem Statement & Project Objectives")

    # Problem Callout
    pbox = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.5))
    pbox.fill.solid()
    pbox.fill.fore_color.rgb = RGBColor(238, 242, 255)
    pbox.line.color.rgb = COLOR_BLUE
    tf_p = pbox.text_frame
    tf_p.margin_left = Inches(0.3)
    tf_p.margin_top = Inches(0.18)
    p = tf_p.paragraphs[0]
    p.text = "🎯 FORMAL PROBLEM STATEMENT"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE
    p2 = tf_p.add_paragraph()
    p2.text = "To design and deploy a complete NLP classification system that ingests unstructured natural language movie reviews, eliminates linguistic noise while preserving sentiment-reversing negations, extracts discriminative n-gram TF-IDF representations, and reliably predicts positive vs. negative sentiment via a high-performance classifier and an interactive web GUI."
    p2.font.size = Pt(13.5)
    p2.font.color.rgb = COLOR_TEXT

    # 4 Objectives
    objs = [
        ("1. Data Pipeline", "Collect & clean 50,000 labelled reviews from the Stanford IMDb benchmark."),
        ("2. Feature Extraction", "Transform text via Sublinear TF-IDF (1, 2)-grams with negation protection."),
        ("3. Model Benchmarking", "Train & compare Naive Bayes, Logistic Regression, and Linear SVM models."),
        ("4. GUI Deployment", "Deliver a responsive Streamlit web application with confidence probabilities.")
    ]
    for i, (otitle, odesc) in enumerate(objs):
        oc = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i*3.0), Inches(3.6), Inches(2.75), Inches(3.1))
        oc.fill.solid()
        oc.fill.fore_color.rgb = COLOR_CARD
        oc.line.color.rgb = COLOR_BORDER
        tf_oc = oc.text_frame
        tf_oc.margin_left = Inches(0.2)
        tf_oc.margin_top = Inches(0.2)
        p = tf_oc.paragraphs[0]
        p.text = otitle
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY
        p_d = tf_oc.add_paragraph()
        p_d.text = "\n" + odesc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_TEXT

    # =========================================================================
    # SLIDE 3: Introduction & Real-World Applications
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "03", "Introduction & Real-World Applications")

    c3_l = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c3_l.fill.solid()
    c3_l.fill.fore_color.rgb = COLOR_CARD
    c3_l.line.color.rgb = COLOR_BORDER
    tf3_l = c3_l.text_frame
    tf3_l.margin_left = Inches(0.3)
    tf3_l.margin_top = Inches(0.25)
    p = tf3_l.paragraphs[0]
    p.text = "Introduction to Sentiment Analysis"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    intro_points = [
        "Core Definition: Sentiment Analysis (Opinion Mining) is the computational study of opinions, sentiments, and emotions expressed in written text.",
        "The Big Data Bottleneck: Movie databases (IMDb, Rotten Tomatoes) host millions of reviews. Manual auditing is physically impossible.",
        "Unstructured to Structured: NLP bridges human expression and computer mathematics by transforming arbitrary prose into normalized feature vectors.",
        "Subtle Linguistic Signals: Accurate sentiment mining requires distinguishing contextual polarity, idioms, and negation syntax."
    ]
    for ip in intro_points:
        p_b = tf3_l.add_paragraph()
        p_b.text = "• " + ip
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT

    c3_r = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c3_r.fill.solid()
    c3_r.fill.fore_color.rgb = COLOR_CARD
    c3_r.line.color.rgb = COLOR_BORDER
    tf3_r = c3_r.text_frame
    tf3_r.margin_left = Inches(0.3)
    tf3_r.margin_top = Inches(0.25)
    p = tf3_r.paragraphs[0]
    p.text = "Industry & Real-World Applications"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE

    apps = [
        "Film & Entertainment Industry: Studios monitor opening weekend reception to adjust marketing campaigns and forecast box-office lifetime gross.",
        "E-Commerce Marketplaces: Amazon, Flipkart, and Google Reviews automatically flag sudden negative feedback spikes indicating defective product batches.",
        "Customer Support Automation: Helps ticketing systems prioritize angry or churn-risk customers for immediate supervisor intervention.",
        "Financial & Brand Intelligence: Algorithmic trading desks mine market sentiment from financial news to detect corporate reputation shifts."
    ]
    for ap in apps:
        p_b = tf3_r.add_paragraph()
        p_b.text = "• " + ap
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT

    # =========================================================================
    # SLIDE 4: Dataset Description
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "04", "Dataset Description & Benchmark Scope")

    c4_l = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c4_l.fill.solid()
    c4_l.fill.fore_color.rgb = COLOR_CARD
    c4_l.line.color.rgb = COLOR_BORDER
    tf4_l = c4_l.text_frame
    tf4_l.margin_left = Inches(0.3)
    tf4_l.margin_top = Inches(0.25)
    p = tf4_l.paragraphs[0]
    p.text = "Stanford IMDb Benchmark (Maas et al., 2011)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    ds_points = [
        "Dataset Volume: Exactly 50,000 highly polarized movie reviews.",
        "Official Training Split: 25,000 reviews (12,500 pos / 12,500 neg).",
        "Official Test Split: 25,000 held-out reviews (12,500 pos / 12,500 neg).",
        "Perfect Balance: 50.0% Positive / 50.0% Negative split eliminates majority-class accuracy bias.",
        "Rating Criteria: Positive (>= 7/10 stars), Negative (<= 4/10 stars).",
        "Disjoint Films: Train and test sets feature disjoint movie titles so models cannot simply memorize film names."
    ]
    for dp in ds_points:
        p_b = tf4_l.add_paragraph()
        p_b.text = "• " + dp
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT

    c4_r = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c4_r.fill.solid()
    c4_r.fill.fore_color.rgb = RGBColor(254, 242, 242)
    c4_r.line.color.rgb = RGBColor(248, 113, 113)
    tf4_r = c4_r.text_frame
    tf4_r.margin_left = Inches(0.3)
    tf4_r.margin_top = Inches(0.25)
    p = tf4_r.paragraphs[0]
    p.text = "Academic Scope: Binary vs. Neutral"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(185, 28, 28)

    scope_points = [
        "Why No Neutral Class? The Stanford researchers deliberately excluded neutral reviews (scores 5-6 out of 10) to create a clean polarity benchmark.",
        "Faculty Approved Scope: The faculty approved formulating this system as a Binary Classifier (Positive vs. Negative).",
        "Academic Rigor: Fabricating or guessing artificial neutral labels without ground-truth labels creates severe label noise.",
        "Full Disclosure: Both the Streamlit GUI and report clearly declare this limitation.",
        "Future Extension: Incorporating the Stanford Sentiment Treebank (SST-3) would be required to train a genuine 3-class model."
    ]
    for sp in scope_points:
        p_b = tf4_r.add_paragraph()
        p_b.text = "• " + sp
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT

    # =========================================================================
    # SLIDE 5: Data Preprocessing and EDA
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "05", "Data Preprocessing & Exploratory Data Analysis (EDA)")

    c5_l = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c5_l.fill.solid()
    c5_l.fill.fore_color.rgb = COLOR_CARD
    c5_l.line.color.rgb = COLOR_BORDER
    tf5_l = c5_l.text_frame
    tf5_l.margin_left = Inches(0.3)
    tf5_l.margin_top = Inches(0.25)
    p = tf5_l.paragraphs[0]
    p.text = "Text Cleaning & Negation Shielding"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    prep_bullets = [
        "HTML Entity & Tag Removal: Regex strips <br />, <i>, &amp; artifacts.",
        "Case Normalization: All reviews converted to lowercase.",
        "Contraction Preservation: Keeps apostrophes (don't, wasn't) so contractions are not corrupted into fragmented tokens.",
        "CRITICAL NEGATION RULE: Standard stopword removal drops 'not', 'no', 'never'. This flips 'movie was not good' into 'movie good'!",
        "Our Solution: A 26-word negation whitelist (not, no, never, didn't, etc.) is strictly shielded from removal."
    ]
    for pb in prep_bullets:
        p_b = tf5_l.add_paragraph()
        p_b.text = "• " + pb
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = COLOR_TEXT

    c5_r = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c5_r.fill.solid()
    c5_r.fill.fore_color.rgb = COLOR_CARD
    c5_r.line.color.rgb = COLOR_BORDER
    tf5_r = c5_r.text_frame
    tf5_r.margin_left = Inches(0.3)
    tf5_r.margin_top = Inches(0.25)
    p = tf5_r.paragraphs[0]
    p.text = "Exploratory Data Analysis Findings"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE

    eda_bullets = [
        "Data Hygiene Audit: Confirmed 0 null values, 0 empty strings, and verified 100% clean UTF-8 text records.",
        "Document Length Analysis: Average review length is ~230 words. Both positive and negative classes share identical length distributions.",
        "Vocabulary Separation: Positive reviews correlate with 'superb', 'great', 'love', 'masterpiece'. Negative reviews correlate with 'awful', 'waste', 'boring', 'terrible'.",
        "Statistical Visualization: Documented in Notebook 03 with seaborn histograms, boxplots, and word frequencies."
    ]
    for eb in eda_bullets:
        p_b = tf5_r.add_paragraph()
        p_b.text = "• " + eb
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = COLOR_TEXT

    # =========================================================================
    # SLIDE 6: Feature Engineering and Methodology
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "06", "Feature Engineering & Methodology")

    c6_l = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c6_l.fill.solid()
    c6_l.fill.fore_color.rgb = COLOR_CARD
    c6_l.line.color.rgb = COLOR_BORDER
    tf6_l = c6_l.text_frame
    tf6_l.margin_left = Inches(0.3)
    tf6_l.margin_top = Inches(0.25)
    p = tf6_l.paragraphs[0]
    p.text = "Bag of Words vs. TF-IDF"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    fe_bullets = [
        "Bag of Words (Baseline): Counts raw term frequencies. Problem: Generic words ('movie', 'one', 'film') dominate the matrix without offering polarity cues.",
        "TF-IDF (Selected): Multiplies Term Frequency (TF) by Inverse Document Frequency (IDF) to scale down common words while boosting informative sentiment words.",
        "Sublinear TF Scaling: Replaces raw TF with 1 + log(tf), preventing excessively repetitive terms from dominating vectors.",
        "Unigrams + Bigrams: (1, 2)-grams capture crucial phrases like 'not good', 'must watch', and 'total waste'."
    ]
    for fb in fe_bullets:
        p_b = tf6_l.add_paragraph()
        p_b.text = "• " + fb
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT

    c6_r = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c6_r.fill.solid()
    c6_r.fill.fore_color.rgb = RGBColor(240, 253, 244)
    c6_r.line.color.rgb = COLOR_GREEN
    tf6_r = c6_r.text_frame
    tf6_r.margin_left = Inches(0.3)
    tf6_r.margin_top = Inches(0.25)
    p = tf6_r.paragraphs[0]
    p.text = "Zero Data Leakage Methodology"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN

    dl_bullets = [
        "Encapsulated Pipeline: Both TfidfVectorizer and Classifier are fused inside a scikit-learn Pipeline.",
        "Fit on Training Data ONLY: The vocabulary (100,000 features) and IDF weights are computed strictly from the training split.",
        "Transform-Only Evaluation: Validation and test partitions are transformed using the pre-fitted pipeline without relearning weights.",
        "Honest Generalization: The test set remained completely untouched until final evaluation."
    ]
    for db in dl_bullets:
        p_b = tf6_r.add_paragraph()
        p_b.text = "• " + db
        p_b.font.size = Pt(12.5)
        p_b.font.color.rgb = COLOR_TEXT

    # =========================================================================
    # SLIDE 7: Model Architecture and Algorithms
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "07", "Model Architecture & Algorithm Benchmarking")

    models_info = [
        ("Multinomial Naive Bayes", "Validation Accuracy: 88.06%  |  Macro F1: 0.8806",
         "Applies Bayes' theorem with the naive feature independence assumption. Extremely fast and lightweight baseline, but struggles with correlated n-gram features.", False),
        ("Logistic Regression (L-BFGS)", "Validation Accuracy: 88.92%  |  Macro F1: 0.8892",
         "Finds a linear decision boundary using log-odds optimization with L2 regularization. Supports well-calibrated native probability outputs (predict_proba).", False),
        ("Linear Support Vector Machine (LinearSVC)", "Validation Accuracy: 90.00%  |  Macro F1: 0.9000  [SELECTED BEST MODEL]",
         "Finds the maximum-margin hyperplane separating positive and negative reviews. Excels in ultra-high dimensional, sparse NLP feature spaces (100,000 TF-IDF features).", True)
    ]
    for i, (mtitle, mstats, mdesc, is_best) in enumerate(models_info):
        mb = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8 + i*1.7), Inches(11.733), Inches(1.45))
        mb.fill.solid()
        if is_best:
            mb.fill.fore_color.rgb = RGBColor(240, 253, 244)
            mb.line.color.rgb = COLOR_GREEN
            c_head = COLOR_GREEN
        else:
            mb.fill.fore_color.rgb = COLOR_CARD
            mb.line.color.rgb = COLOR_BORDER
            c_head = COLOR_NAVY

        tf_mb = mb.text_frame
        tf_mb.margin_left = Inches(0.3)
        tf_mb.margin_top = Inches(0.15)
        p = tf_mb.paragraphs[0]
        p.text = mtitle
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = c_head

        p_st = tf_mb.add_paragraph()
        p_st.text = mstats
        p_st.font.size = Pt(13)
        p_st.font.bold = True
        p_st.font.color.rgb = COLOR_TEXT

        p_ds = tf_mb.add_paragraph()
        p_ds.text = mdesc
        p_ds.font.size = Pt(11.5)
        p_ds.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 8: Performance Evaluation and Results
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_header(s8, "08", "Performance Evaluation & Held-Out Test Results")

    # Left: Stats
    card_e = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.0), Inches(4.8))
    card_e.fill.solid()
    card_e.fill.fore_color.rgb = COLOR_CARD
    card_e.line.color.rgb = COLOR_BORDER
    tf_e = card_e.text_frame
    tf_e.margin_left = Inches(0.3)
    tf_e.margin_top = Inches(0.25)
    p = tf_e.paragraphs[0]
    p.text = "Held-Out Test Set Metrics (n = 25,000)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    eval_stats = [
        "Overall Test Accuracy: 89.90% (22,474 / 25,000 correct)",
        "Negative Reviews: Precision = 89.84% | Recall = 89.98% | F1 = 89.91%",
        "Positive Reviews: Precision = 89.96% | Recall = 89.82% | F1 = 89.89%",
        "Macro Average F1-Score: 0.8990 (Near-perfect parity across both classes)",
        "True Negatives: 11,247  |  True Positives: 11,227",
        "False Positives: 1,253  |  False Negatives: 1,273",
        "Zero Overfitting: Validation accuracy (90.00%) closely matches test accuracy (89.90%)."
    ]
    for es in eval_stats:
        p_b = tf_e.add_paragraph()
        p_b.text = "• " + es
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = COLOR_TEXT

    # Right: Embedded Confusion Matrix Image
    cm_path = os.path.join(base_dir, "confusion_matrix.png")
    if os.path.exists(cm_path):
        s8.shapes.add_picture(cm_path, Inches(7.2), Inches(1.8), width=Inches(5.3))

    # =========================================================================
    # SLIDE 9: GUI Screenshots and Working Demonstration
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_header(s9, "09", "GUI Screenshots & Working Demonstration")

    # Left: Features
    card_g = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.3), Inches(4.8))
    card_g.fill.solid()
    card_g.fill.fore_color.rgb = COLOR_CARD
    card_g.line.color.rgb = COLOR_BORDER
    tf_g = card_g.text_frame
    tf_g.margin_left = Inches(0.3)
    tf_g.margin_top = Inches(0.2)
    p = tf_g.paragraphs[0]
    p.text = "Interactive Streamlit Web Features"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    gui_pts = [
        "SaaS-Grade Visuals: Modern dark hero header, badges, and smooth responsive layout.",
        "1-Click Sample Benchmarks: Test positive, negative, tricky negation, and mixed reviews with one click.",
        "Dynamic Confidence Gauge: Displays model confidence % with calibrated sigmoid distribution bar.",
        "Linguistic Preprocessing Tab: Compares raw vs cleaned text and flags preserved negation tokens with badges.",
        "Embedded Confusion Matrix Tab: Allows faculty to inspect evaluation evidence directly inside the web app."
    ]
    for gp in gui_pts:
        p_b = tf_g.add_paragraph()
        p_b.text = "• " + gp
        p_b.font.size = Pt(11.5)
        p_b.font.color.rgb = COLOR_TEXT

    # Right: Embedded GUI Showcase Image
    gui_img = os.path.join(base_dir, "gui_showcase.png")
    if os.path.exists(gui_img):
        s9.shapes.add_picture(gui_img, Inches(6.4), Inches(1.8), width=Inches(6.1))

    # =========================================================================
    # SLIDE 10: Conclusion and Future Scope
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_header(s10, "10", "Conclusion & Future Scope")

    c10_l = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c10_l.fill.solid()
    c10_l.fill.fore_color.rgb = RGBColor(240, 253, 244)
    c10_l.line.color.rgb = COLOR_GREEN
    tf10_l = c10_l.text_frame
    tf10_l.margin_left = Inches(0.3)
    tf10_l.margin_top = Inches(0.25)
    p = tf10_l.paragraphs[0]
    p.text = "Key Project Achievements"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN

    concl_pts = [
        "10-Stage Completion: Built every stage from scratch following strict academic NLP standards.",
        "High Generalization: Attained 89.90% test accuracy on 25,000 unseen reviews using TF-IDF + Linear SVM.",
        "Linguistic Integrity: Solved negation inversion trap ('not good') via custom whitelist filters.",
        "Zero Data Leakage: Ensured rigorous pipeline isolation between train and test splits.",
        "Working GUI: Delivered a functional, elegant Streamlit web app satisfying faculty mandate."
    ]
    for cp in concl_pts:
        p_b = tf10_l.add_paragraph()
        p_b.text = "• " + cp
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = COLOR_TEXT

    c10_r = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c10_r.fill.solid()
    c10_r.fill.fore_color.rgb = RGBColor(238, 242, 255)
    c10_r.line.color.rgb = COLOR_BLUE
    tf10_r = c10_r.text_frame
    tf10_r.margin_left = Inches(0.3)
    tf10_r.margin_top = Inches(0.25)
    p = tf10_r.paragraphs[0]
    p.text = "Future Research & Enhancements"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE

    fut_pts = [
        "Contextual Transformer Models: Fine-tuning BERT, DistilBERT, or RoBERTa for complex rhetorical comprehension.",
        "Three-Class Classification: Training on the Stanford Sentiment Treebank (SST-3) to incorporate genuine neutral sentiments.",
        "Aspect-Based Sentiment: Identifying sentiment toward specific dimensions (e.g. 'acting was great, but music was loud').",
        "Cross-Domain Generalization: Adapting model weights to product and restaurant review domains."
    ]
    for fp in fut_pts:
        p_b = tf10_r.add_paragraph()
        p_b.text = "• " + fp
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = COLOR_TEXT

    # =========================================================================
    # SLIDE 11: Viva Voce & Q&A
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    bg11 = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg11.fill.solid()
    bg11.fill.fore_color.rgb = COLOR_NAVY
    bg11.line.color.rgb = COLOR_NAVY

    tbox11 = s11.shapes.add_textbox(Inches(1.5), Inches(1.8), Inches(10.333), Inches(4.2))
    tf11 = tbox11.text_frame
    tf11.word_wrap = True

    p = tf11.paragraphs[0]
    p.text = "Thank You!"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    p2 = tf11.add_paragraph()
    p2.text = "\nMovie Review Sentiment Analysis using NLP & Machine Learning"
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(147, 197, 253)
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf11.add_paragraph()
    p3.text = "\nAchieved 89.90% Test Accuracy · Tested on 25,000 Unseen Reviews · Live Streamlit Web App"
    p3.font.size = Pt(15)
    p3.font.color.rgb = RGBColor(226, 232, 240)
    p3.alignment = PP_ALIGN.CENTER

    p4 = tf11.add_paragraph()
    p4.text = "\nReady for Faculty Evaluation & Viva Voce Q&A"
    p4.font.size = Pt(16)
    p4.font.bold = True
    p4.font.color.rgb = RGBColor(74, 222, 128)
    p4.alignment = PP_ALIGN.CENTER

    # Save Presentation
    prs.save(output_path)
    print(f"Updated 10-Point PPTX generated successfully: {output_path}")

if __name__ == "__main__":
    out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Movie_Sentiment_Analysis_Presentation.pptx")
    build_presentation(out_file)
