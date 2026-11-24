# SpamBam — Spam Email Detector

A school-project implementation using Python, scikit-learn, and Streamlit, with a matching Orange Data Mining workflow.

## What is included
- `app.py` — Streamlit website for checking a message.
- `Python/` — model-training script, dataset downloader, and prediction helper.
- `Dataset/` — expected location for the SpamAssassin CSV and dataset notes.
- `Orange/` — Orange workflow instructions and recorded evaluation.
- `Results/` — actual evaluation figures already obtained during this project.
- `Documentation/` — project report outline, logbook template, and video outline.

## First-time setup (Windows)
Open this folder in VS Code, then open **Terminal → New Terminal**.

```powershell
python -m pip install -r requirements.txt
python Python/download_dataset.py
python app.py
```

The website will open in your browser. If it does not, use the local URL printed in the terminal (normally `http://localhost:8501`).

## Dataset
The project expects `Dataset/raw/SA_SubTxt_fn.csv` with columns:
- `label`: 0 = ham (not spam), 1 = spam
- `data`: email/message text
- `filename`: message identifier (not used as model text)

The download script retrieves the CSV from the Hugging Face dataset repository. If you already have the CSV, copy it into `Dataset/raw/` instead.

## Important
- Do not describe the recorded test metrics as a guarantee that every future email will be classified correctly.
- The Python test split and Orange 5-fold cross-validation are separate evaluations; keep their results separate.
- Orange results in `Results/` are the values recorded from the completed Orange workflow.
