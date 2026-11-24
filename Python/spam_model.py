from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


def clean_text(value):
    """Convert a cell to safe plain text; tolerate missing/non-string values."""
    if pd.isna(value):
        return ""
    if isinstance(value, (list, tuple)):
        return " ".join(str(item) for item in value)
    return str(value)


def load_dataset(csv_path):
    """Load and validate the SpamBam CSV."""
    frame = pd.read_csv(csv_path)
    required = {"label", "data"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(
            f"Dataset is missing required column(s): {', '.join(sorted(missing))}. "
            "Expected columns: label and data."
        )

    frame = frame[["label", "data"]].copy()
    frame["data"] = frame["data"].map(clean_text)
    frame["label"] = pd.to_numeric(frame["label"], errors="coerce")
    frame = frame.dropna(subset=["label"])
    frame["label"] = frame["label"].astype(int)
    frame = frame[frame["label"].isin([0, 1])]
    frame = frame[frame["data"].str.strip().ne("")]
    if frame.empty:
        raise ValueError("No usable labelled messages were found in the CSV.")
    return frame.reset_index(drop=True)


def build_pipeline():
    """Bag of Words + Multinomial Naive Bayes."""
    return Pipeline([
        ("vectorizer", CountVectorizer(stop_words="english", max_features=5000)),
        ("classifier", MultinomialNB()),
    ])


if __name__ == "__main__":
    print("Import load_dataset() and build_pipeline() from this module.")
