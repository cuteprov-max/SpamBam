# Orange Data Mining workflow

Use Orange Data Mining with the Text Mining add-on.

## Workflow
`File → Select Columns → Corpus → Preprocess Text → Bag of Words → Test & Score`

Connect `Naive Bayes` to `Test & Score` as the Learner, and connect `Test & Score` to `Confusion Matrix`.

## Important widget settings
- In **Select Columns**, set `label` as Target.
- Keep `data` as the text field.
- Keep `filename` as a title/meta field; do not use it as message text.
- In **Corpus**, set `filename` as Title variable and `data` as the used text feature.
- Set language to **English**.
- Use **Stratified 5-fold cross-validation** in Test & Score.
- Use Naive Bayes as the learner.

## Recorded Orange evaluation
The completed workflow recorded:
- AUC: 0.995
- CA / Accuracy: 0.979 (97.9%)
- F1: 0.985 (98.5%)
- Precision: 0.989 (98.9%)
- Recall: 0.980 (98.0%)
- MCC: 0.951

Confusion matrix (actual rows, predicted columns; class 0 = ham, class 1 = spam):

| Actual \ Predicted | Ham (0) | Spam (1) |
|---|---:|---:|
| Ham (0) | 4069 | 81 |
| Spam (1) | 47 | 1849 |

These are Orange's recorded 5-fold cross-validation results. Do not mix them with the separate Python hold-out test.
