from pathlib import Path
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    precision_score, recall_score, f1_score
)
from spam_model import load_dataset, build_pipeline

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Dataset" / "raw" / "SA_SubTxt_fn.csv"
MODEL_DIR = ROOT / "Python" / "model"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

if not DATA.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA}\nRun: python Python/download_dataset.py"
    )

df = load_dataset(DATA)
X_train, X_test, y_train, y_test = train_test_split(
    df["data"], df["label"], test_size=0.20, random_state=42, stratify=df["label"]
)

model = build_pipeline()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

results = {
    "dataset_rows": int(len(df)),
    "train_rows": int(len(X_train)),
    "test_rows": int(len(X_test)),
    "accuracy": float(accuracy_score(y_test, predictions)),
    "precision_weighted": float(precision_score(y_test, predictions, average="weighted", zero_division=0)),
    "recall_weighted": float(recall_score(y_test, predictions, average="weighted", zero_division=0)),
    "f1_weighted": float(f1_score(y_test, predictions, average="weighted", zero_division=0)),
    "confusion_matrix_labels_0_ham_1_spam": confusion_matrix(y_test, predictions, labels=[0, 1]).tolist(),
    "classification_report": classification_report(
        y_test, predictions, target_names=["Ham", "Spam"], output_dict=True, zero_division=0
    ),
}

joblib.dump(model, MODEL_DIR / "spam_bam_model.joblib")
(MODEL_DIR / "python_test_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")

print(json.dumps(results, indent=2))
print(f"\nSaved model to: {MODEL_DIR / 'spam_bam_model.joblib'}")
