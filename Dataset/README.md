# Dataset

Expected file: `raw/SA_SubTxt_fn.csv`

Source: Hugging Face dataset repository `bvk/SpamAssassin-spam`, based on the SpamAssassin public mail corpus.

Expected fields:
- `label`: 0 = ham, 1 = spam
- `data`: email/message text
- `filename`: source message identifier

The model uses only `data` as input and `label` as the target. `filename` is not a text feature.

Download using:

```bash
python Python/download_dataset.py
```

The dataset is not duplicated in this project ZIP. Keep the downloaded CSV in `Dataset/raw/`.
