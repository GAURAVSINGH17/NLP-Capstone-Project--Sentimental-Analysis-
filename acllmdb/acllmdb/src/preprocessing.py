"""
src/preprocessing.py
--------------------
Text preprocessing utilities for movie review sentiment analysis.

Design decisions
~~~~~~~~~~~~~~~~
1.  HTML tag removal:   IMDb reviews contain <br /> tags and occasional HTML
    entities (e.g. &amp;).  These are not linguistic content and should be
    removed before analysis.

2.  Lowercase normalisation:   Reduces vocabulary size without losing meaning.

3.  Negation preservation:     Words like "not", "no", "never", "n't" carry
    crucial sentiment information.  They are intentionally kept even when
    stopword removal is applied.

4.  Stopword removal:          Optional.  When enabled, common English
    stopwords are removed EXCEPT negation words (see NEGATION_WORDS below).
    For TF-IDF + sklearn pipelines, stopword handling can also be done
    inside TfidfVectorizer; this module provides an alternative if needed.

5.  Stemming / Lemmatisation:  NOT applied by default.  Aggressive stemming
    can conflate words with different sentiment (e.g. "good" / "goods") and
    is not needed for a TF-IDF + linear classifier baseline.

For the baseline model, the TfidfVectorizer handles tokenisation
internally.  This module is used in the EDA/notebook stages and can be
plugged in as a custom preprocessor if desired.
"""

import re
import html

# ---------------------------------------------------------------------------
# Precompiled Regexes for high-performance batch processing
# ---------------------------------------------------------------------------
TAG_RE = re.compile(r"<[^>]+>")
NON_ALPHA_RE = re.compile(r"[^a-z\s']")
SPACE_RE = re.compile(r"\s+")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# These negation words must NOT be removed as stopwords.
NEGATION_WORDS = {
    "no", "not", "nor", "never", "neither", "nobody", "nothing",
    "nowhere", "none", "cannot", "can't", "won't", "don't", "didn't",
    "doesn't", "isn't", "aren't", "wasn't", "weren't", "hasn't",
    "haven't", "hadn't", "wouldn't", "shouldn't", "couldn't", "mightn't",
    "mustn't", "needn't",
}

# ---------------------------------------------------------------------------
# Core preprocessing function
# ---------------------------------------------------------------------------

def clean_review(text: str, remove_stopwords: bool = False) -> str:
    """
    Clean a single movie review text.

    Steps applied (in order):
      1. Decode HTML entities  (e.g. &amp; -> &)
      2. Remove HTML tags      (e.g. <br />, <i>)
      3. Lowercase
      4. Remove non-alphabetic characters except apostrophes
         (preserves contractions like "don't", "wasn't")
      5. Collapse multiple whitespace to a single space
      6. (Optional) Remove stopwords, keeping NEGATION_WORDS

    Parameters
    ----------
    text             : Raw review string
    remove_stopwords : If True, remove common English stopwords,
                       but always keep NEGATION_WORDS.

    Returns
    -------
    Cleaned string
    """
    if not isinstance(text, str):
        return ""

    # 1. Decode HTML entities
    text = html.unescape(text)

    # 2. Remove HTML tags
    text = TAG_RE.sub(" ", text)

    # 3. Lowercase
    text = text.lower()

    # 4. Keep letters and apostrophes only
    text = NON_ALPHA_RE.sub(" ", text)

    # 5. Collapse whitespace
    text = SPACE_RE.sub(" ", text).strip()

    # 6. Optional stopword removal (negation words are always kept)
    if remove_stopwords:
        try:
            from nltk.corpus import stopwords as nltk_stopwords
            sw = set(nltk_stopwords.words("english")) - NEGATION_WORDS
            tokens = text.split()
            tokens = [t for t in tokens if t not in sw]
            text = " ".join(tokens)
        except LookupError:
            pass

    return text

    # 6. Optional stopword removal (negation words are always kept)
    if remove_stopwords:
        try:
            from nltk.corpus import stopwords as nltk_stopwords
            sw = set(nltk_stopwords.words("english")) - NEGATION_WORDS
            tokens = text.split()
            tokens = [t for t in tokens if t not in sw]
            text = " ".join(tokens)
        except LookupError:
            # NLTK data not downloaded yet; skip stopword removal silently
            pass

    return text


def apply_cleaning(series, remove_stopwords: bool = False):
    """
    Apply clean_review to a Pandas Series of review texts.

    Parameters
    ----------
    series           : pd.Series of raw review strings
    remove_stopwords : Passed through to clean_review()

    Returns
    -------
    pd.Series of cleaned strings
    """
    return series.apply(lambda t: clean_review(t, remove_stopwords=remove_stopwords))
