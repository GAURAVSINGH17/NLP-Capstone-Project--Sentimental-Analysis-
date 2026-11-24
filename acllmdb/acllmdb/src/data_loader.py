"""
src/data_loader.py
------------------
Utility functions to load the Stanford IMDb Large Movie Review Dataset
(aclImdb) into a Pandas DataFrame.

The dataset folder structure is:
    aclImdb/
        train/pos/   <-- 12,500 positive training reviews
        train/neg/   <-- 12,500 negative training reviews
        test/pos/    <-- 12,500 positive test reviews
        test/neg/    <-- 12,500 negative test reviews

Labels are derived from the folder name, NOT from the review text.
  - pos  -> sentiment = "positive", label = 1
  - neg  -> sentiment = "negative", label = 0

The train/unsup folder is NOT loaded because it has no labels.
"""

import os
import pandas as pd

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _load_split(split_dir: str, split_name: str) -> pd.DataFrame:
    """
    Load all positive and negative .txt files from one split directory.

    Parameters
    ----------
    split_dir  : Absolute path to the split directory (e.g. .../aclImdb/train)
    split_name : 'train' or 'test'

    Returns
    -------
    pd.DataFrame with columns: review, sentiment, label, split
    """
    records = []
    for sentiment_folder, sentiment_str, numeric_label in [
        ("pos", "positive", 1),
        ("neg", "negative", 0),
    ]:
        folder_path = os.path.join(split_dir, sentiment_folder)
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(
                f"Expected folder not found: {folder_path}. "
                "Check that the aclImdb dataset is at the expected location."
            )
        for filename in os.listdir(folder_path):
            if not filename.endswith(".txt"):
                continue
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as fh:
                    text = fh.read()
            except UnicodeDecodeError:
                # Fallback: some reviews may contain non-UTF-8 bytes
                with open(filepath, "r", encoding="latin-1") as fh:
                    text = fh.read()
            records.append(
                {
                    "review": text,
                    "sentiment": sentiment_str,
                    "label": numeric_label,
                    "split": split_name,
                }
            )
    return pd.DataFrame(records)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_imdb_dataset(dataset_root: str) -> pd.DataFrame:
    """
    Load both train and test labelled splits of the IMDb aclImdb dataset.

    Parameters
    ----------
    dataset_root : Path to the aclImdb directory, e.g.
                   r"C:\\...\\movie sentiment analysis\\aclImdb"

    Returns
    -------
    pd.DataFrame with columns: review, sentiment, label, split
        - split == 'train'  -> 25,000 rows (12,500 pos + 12,500 neg)
        - split == 'test'   -> 25,000 rows (12,500 pos + 12,500 neg)
    """
    train_df = _load_split(os.path.join(dataset_root, "train"), "train")
    test_df  = _load_split(os.path.join(dataset_root, "test"),  "test")
    df = pd.concat([train_df, test_df], ignore_index=True)
    return df


def get_train_test(df: pd.DataFrame):
    """
    Split a combined DataFrame into train and test subsets.

    Parameters
    ----------
    df : DataFrame returned by load_imdb_dataset()

    Returns
    -------
    (train_df, test_df)
    """
    train_df = df[df["split"] == "train"].reset_index(drop=True)
    test_df  = df[df["split"] == "test"].reset_index(drop=True)
    return train_df, test_df
