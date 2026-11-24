"""
app.py
------
Interactive Streamlit Application for Movie Review Sentiment Analysis.
Academic NLP & Machine Learning Project.
"""

import os
import sys
import numpy as np
import joblib
import streamlit as st

# ---------------------------------------------------------------------------
# Path & Environment Setup
# ---------------------------------------------------------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(APP_DIR, "models", "sentiment_pipeline.joblib")
CONFUSION_MATRIX_PATH = os.path.join(APP_DIR, "confusion_matrix.png")

sys.path.insert(0, APP_DIR)
from src.preprocessing import clean_review, NEGATION_WORDS

# ---------------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="CineSense | Movie Sentiment Analyzer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Custom CSS Styling (Clean, Modern, Professional SaaS-like Design)
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero Header Card */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        max-width: 800px;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    .badge-pill {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-right: 0.5rem;
        margin-bottom: 0.3rem;
    }
    .badge-blue { background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
    .badge-green { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); }
    .badge-purple { background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }

    /* Result Cards */
    .result-card {
        padding: 1.75rem;
        border-radius: 16px;
        margin-top: 1.5rem;
        animation: fadeIn 0.4s ease-in-out;
    }
    .result-positive {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.08) 0%, rgba(16, 185, 129, 0.12) 100%);
        border: 2px solid #22c55e;
    }
    .result-negative {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.08) 0%, rgba(244, 63, 94, 0.12) 100%);
        border: 2px solid #ef4444;
    }
    .result-heading {
        font-size: 1.75rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }
    .pos-text { color: #15803d; }
    .neg-text { color: #b91c1c; }

    /* Metric Cards */
    .metric-box {
        background: white;
        padding: 1.25rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        text-align: center;
    }
    .metric-value {
        font-size: 1.75rem;
        font-weight: 800;
        color: #0f172a;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
    }

    /* Highlight badge for negation tokens */
    .neg-token {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 600;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Cached Model Loader
# ---------------------------------------------------------------------------
@st.cache_resource(show_spinner="Loading NLP Sentiment Pipeline...")
def load_sentiment_pipeline(path: str):
    """Load and cache the trained scikit-learn Pipeline."""
    return joblib.load(path)

def get_prediction_and_confidence(pipeline, text: str):
    """
    Given a preprocessed review, compute prediction label and confidence score.
    Uses predict_proba if available, or calibrated sigmoid on decision_function.
    """
    clf = pipeline.named_steps.get("clf")
    pred_label = pipeline.predict([text])[0]  # 0: Negative, 1: Positive
    
    if hasattr(clf, "predict_proba"):
        proba = pipeline.predict_proba([text])[0]
    elif hasattr(clf, "decision_function"):
        score = pipeline.decision_function([text])[0]
        # Sigmoid calibration: 1 / (1 + exp(-score))
        prob_pos = float(1.0 / (1.0 + np.exp(-score)))
        prob_neg = float(1.0 - prob_pos)
        proba = np.array([prob_neg, prob_pos])
    else:
        proba = np.array([0.5, 0.5])
        
    confidence = float(proba[pred_label])
    return pred_label, confidence, proba

# ---------------------------------------------------------------------------
# Sidebar: Academic Information & Model Specs
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎓 Academic Information")
    st.markdown(
        """
        - **Course:** Natural Language Processing (NLP)
        - **Task:** Binary Sentiment Classification
        - **Dataset:** Stanford IMDb (`aclImdb`)
        - **Benchmark Size:** 50,000 labelled reviews
        """
    )
    
    st.divider()
    st.markdown("### ⚙️ Model Architecture")
    st.markdown(
        """
        - **Vectorizer:** TF-IDF (Unigrams + Bigrams)
        - **Max Features:** 100,000 vocabulary size
        - **Classifier:** Linear Support Vector Machine
        - **Test Accuracy:** **89.90%** (on 25k test set)
        - **Macro F1-Score:** **0.8990**
        """
    )
    
    st.divider()
    st.markdown("### 💡 Quick Sample Reviews")
    st.caption("Click any button below to test a sample review:")
    
    sample_1 = "The movie was absolutely fantastic! The acting was superb, the screenplay was sharp, and the cinematography was breathtaking. Highly recommended to everyone."
    sample_2 = "A complete waste of time. The script made no sense, the pacing was agonizingly slow, and the performances were completely unconvincing and wooden."
    sample_3 = "I expected this movie to be good, but it was not good at all. I did not like the characters and never felt engaged."
    sample_4 = "Visually stunning special effects, but the storyline lacked any real emotional depth. Still quite enjoyable for an action flick."
    
    if st.button("🌟 Positive Review Sample", use_container_width=True):
        st.session_state["review_input"] = sample_1
    if st.button("❌ Negative Review Sample", use_container_width=True):
        st.session_state["review_input"] = sample_2
    if st.button("⚡ Tricky Negation Sample", use_container_width=True):
        st.session_state["review_input"] = sample_3
    if st.button("⚖️ Mixed Review Sample", use_container_width=True):
        st.session_state["review_input"] = sample_4
        
    st.divider()
    st.caption("Created for NLP Semester Project · Streamlit & Scikit-Learn")

# ---------------------------------------------------------------------------
# Main Content Area
# ---------------------------------------------------------------------------

# Hero Banner
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">🎬 CineSense: Movie Review Sentiment Analysis</div>
        <div class="hero-subtitle">
            An end-to-end Machine Learning and NLP system trained on the Stanford IMDb dataset. 
            Enter any film review to inspect its sentiment classification, confidence probability, 
            and token-level linguistic preprocessing.
        </div>
        <div>
            <span class="badge-pill badge-blue">NLP Pipeline</span>
            <span class="badge-pill badge-green">89.9% Test Accuracy</span>
            <span class="badge-pill badge-purple">TF-IDF + Linear SVM</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Academic Scope Notice
with st.expander("ℹ️ Academic Scope & Class Disclosure", expanded=False):
    st.markdown(
        r"""
        **Scope Disclosure:** This model is strictly a **binary classifier** (*Positive* vs. *Negative*).  
        The Stanford IMDb dataset provides reviews labelled solely as **positive** ($\ge 7/10$) or **negative** ($\le 4/10$), 
        with neutral reviews intentionally omitted by Maas et al. (2011). In adherence to academic integrity, this application 
        does not fabricate or guess a "Neutral" class.
        """
    )

# Model Availability Verification
if not os.path.isfile(MODEL_PATH):
    st.error(
        f"🚨 **Trained Model Pipeline Not Found!**\n\n"
        f"Expected path: `{MODEL_PATH}`\n\n"
        f"Please run the training script in your terminal:\n"
        f"```bash\npython train_model.py\n```"
    )
    st.stop()

pipeline = load_sentiment_pipeline(MODEL_PATH)

# Input Section
st.markdown("### 📝 Enter Movie Review")
col_input, col_meta = st.columns([3, 1])

# Session state initialization
if "review_input" not in st.session_state:
    st.session_state["review_input"] = ""

review_text = st.text_area(
    label="Review Text Area",
    value=st.session_state["review_input"],
    placeholder="Type or paste your movie review here (e.g., 'The performance was stellar and the storyline kept me hooked from beginning to end!')...",
    height=160,
    label_visibility="collapsed",
)

col_btn1, col_btn2, col_spacer = st.columns([1.5, 1, 3])
with col_btn1:
    predict_clicked = st.button("🔍 Analyze Sentiment", type="primary", use_container_width=True)
with col_btn2:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state["review_input"] = ""
        st.rerun()

# ---------------------------------------------------------------------------
# Prediction & Results Display
# ---------------------------------------------------------------------------
if predict_clicked:
    if not review_text or not review_text.strip():
        st.warning("⚠️ **Input Validation:** Please enter a movie review before clicking Analyze.")
    else:
        # Preprocessing
        cleaned_text = clean_review(review_text)
        
        # Inference
        pred_label, confidence, proba = get_prediction_and_confidence(pipeline, cleaned_text)
        sentiment_str = "Positive" if pred_label == 1 else "Negative"
        card_class = "result-positive" if pred_label == 1 else "result-negative"
        text_color_class = "pos-text" if pred_label == 1 else "neg-text"
        sentiment_icon = "😊" if pred_label == 1 else "😞"
        
        # Main Result Card
        st.markdown(
            f"""
            <div class="result-card {card_class}">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span style="font-size:0.9rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:#64748b;">
                            Predicted Polarity
                        </span>
                        <div class="result-heading {text_color_class}">
                            {sentiment_icon} {sentiment_str} Sentiment
                        </div>
                    </div>
                    <div style="text-align:right;">
                        <span style="font-size:0.9rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:#64748b;">
                            Confidence Score
                        </span>
                        <div style="font-size:2rem; font-weight:800; color:#0f172a;">
                            {confidence:.1%}
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Key Metrics Row
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-label">Predicted Class</div>
                    <div class="metric-value {text_color_class}">{sentiment_str}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col_m2:
            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-label">Model Confidence</div>
                    <div class="metric-value">{confidence:.1%}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col_m3:
            neg_p, pos_p = proba[0], proba[1]
            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-label">Positive / Negative Split</div>
                    <div class="metric-value">{pos_p:.0%} / {neg_p:.0%}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Polarity Progress Bar
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Polarity Probability Distribution:**")
        st.progress(float(proba[1]))
        col_bar_l, col_bar_r = st.columns(2)
        col_bar_l.caption(f"🔴 Negative: **{proba[0]:.1%}**")
        col_bar_r.markdown(f"<div style='text-align:right; font-size:0.85rem; color:#64748b;'>🟢 Positive: <b>{proba[1]:.1%}</b></div>", unsafe_allow_html=True)
        
        # Diagnostic & Linguistic Tabs
        st.markdown("<br>", unsafe_allow_html=True)
        tab_inspect, tab_insights, tab_eval = st.tabs(["🔍 Linguistic Preprocessing", "🧠 NLP Pipeline Inspection", "📊 Model Evaluation Evidence"])
        
        with tab_inspect:
            st.markdown("#### Text Cleaning & Negation Preservation Audit")
            st.markdown(
                """
                Our preprocessing pipeline strips HTML tags, lowercases the text, and collapses whitespace, 
                **while strictly preserving sentiment-altering negation terms** (`not`, `no`, `never`, `didn't`, etc.).
                """
            )
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                st.markdown("**Original Raw Input:**")
                st.info(review_text)
            with col_t2:
                st.markdown("**Preprocessed Input (fed to TF-IDF vectorizer):**")
                # Highlight detected negation words in preprocessed text
                tokens = cleaned_text.split()
                highlighted_html = " ".join(
                    [f"<span class='neg-token'>{t}</span>" if t in NEGATION_WORDS else t for t in tokens]
                )
                st.markdown(
                    f"<div style='background:#f8fafc; padding:1rem; border-radius:8px; border:1px solid #e2e8f0; line-height:1.7;'>{highlighted_html}</div>",
                    unsafe_allow_html=True,
                )
                found_negs = [t for t in set(tokens) if t in NEGATION_WORDS]
                if found_negs:
                    st.success(f"🛡️ Preserved Negation Terms: `{', '.join(found_negs)}`")
                else:
                    st.caption("No negation modifiers detected in this review.")

        with tab_insights:
            st.markdown("#### How the Pipeline Arrived at this Prediction")
            st.markdown(
                r"""
                1. **Tokenization & N-Gram Generation:** Text is decomposed into unigrams (single words) and bigrams (two-word phrases).
                2. **Sublinear TF-IDF Transformation:** Word counts are scaled via logarithmic dampening ($1 + \log(\text{tf})$) and penalised by inverse document frequency (IDF).
                3. **Linear SVM Decision Plane:** The high-dimensional feature vector is evaluated against the hyperplane learned during training.
                """
            )
            st.write({
                "Total Characters (Raw)": len(review_text),
                "Total Words (Raw)": len(review_text.split()),
                "Cleaned Words (Tokens)": len(cleaned_text.split()),
                "Classifier": pipeline.named_steps["clf"].__class__.__name__,
                "Vectorizer": pipeline.named_steps["tfidf"].__class__.__name__,
            })

        with tab_eval:
            st.markdown("#### Benchmark Evaluation on Held-Out Test Set (25,000 Reviews)")
            if os.path.isfile(CONFUSION_MATRIX_PATH):
                st.image(CONFUSION_MATRIX_PATH, caption="Confusion Matrix on Official 25,000 IMDb Test Set", width=500)
            st.markdown(
                """
                | Metric | Negative Reviews | Positive Reviews | Macro Average |
                |---|:---:|:---:|:---:|
                | **Precision** | 89.84% | 89.96% | 89.90% |
                | **Recall** | 89.98% | 89.82% | 89.90% |
                | **F1-Score** | 89.91% | 89.89% | **89.90%** |
                | **Overall Test Accuracy** | — | — | **89.90%** |
                """
            )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption(
    "🎬 **Movie Sentiment Analysis** · Semester 5 NLP Project · "
    "Implemented with Python, Scikit-Learn, and Streamlit · "
    "Benchmark Dataset: Maas et al. (Stanford AI Lab)"
)
