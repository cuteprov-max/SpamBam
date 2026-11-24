from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "Dataset" / "raw" / "SA_SubTxt_fn.csv"
URL = (
    "https://huggingface.co/datasets/bvk/SpamAssassin-spam/"
    "resolve/main/SA_SubTxt_fn.csv"
)

DEST.parent.mkdir(parents=True, exist_ok=True)

if DEST.exists():
    print(f"Dataset already exists: {DEST}")
else:
    print("Downloading the SpamAssassin CSV…")
    urlretrieve(URL, DEST)
    print(f"Saved dataset to: {DEST}")
