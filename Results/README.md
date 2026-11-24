# SpamBam results

## Orange — Stratified 5-fold cross-validation
| Metric | Recorded value |
|---|---:|
| AUC | 0.995 |
| CA / Accuracy | 0.979 (97.9%) |
| F1 | 0.985 (98.5%) |
| Precision | 0.989 (98.9%) |
| Recall | 0.980 (98.0%) |
| MCC | 0.951 |

Confusion matrix (actual rows, predicted columns):

| Actual \ Predicted | Predicted Ham | Predicted Spam |
|---|---:|---:|
| Actual Ham | 4069 | 81 |
| Actual Spam | 47 | 1849 |

Total: 5,918 correct out of 6,046; 128 incorrect.

## Python — separate 80:20 hold-out split
Previously recorded confusion matrix (actual rows, predicted columns; 0 = ham, 1 = spam):

```text
[[817, 14],
 [ 24,355]]
```

The reproducible `Python/train_model.py` script calculates and prints the exact metrics for the CSV available on the student's computer. Use that fresh output for the Python practical report. Do not copy Orange metrics into the Python results section.

## Interpretation
The results indicate strong performance on the evaluated dataset. They do not guarantee perfect classification on new or deliberately disguised messages. Dataset quality, class balance, and changes in spam patterns can affect performance.
