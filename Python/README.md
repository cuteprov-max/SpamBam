# Python implementation

## Model
1. Load the labelled CSV.
2. Keep `data` as message text and `label` as the target.
3. Split into training and test sets (80:20, stratified, random_state=42).
4. Convert text to Bag-of-Words features using `CountVectorizer`.
5. Train `MultinomialNB`.
6. Evaluate on the held-out test set.

## Run
From the project root:

```bash
python Python/download_dataset.py
python Python/train_model.py
```

The training script prints the actual metrics for the local dataset and saves the fitted model and JSON results under `Python/model/`.

The Streamlit app trains its own in-memory model when it starts. Run it with `python -m streamlit run app.py` (or `python app.py` as described in the root README).
