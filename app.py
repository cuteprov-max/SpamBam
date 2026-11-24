from pathlib import Path
import sys

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "Python"))

from spam_model import load_dataset, build_pipeline, clean_text

DATA_PATH = ROOT / "Dataset" / "raw" / "SA_SubTxt_fn.csv"

st.set_page_config(
    page_title="SpamBam | Email Checker",
    page_icon="🛡️",
    layout="centered",
)


st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: #101827;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #FF8C00 !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #1B2638;
    }

    /* Buttons */
    .stButton > button {
        background-color: #FF8C00;
        color: #101827;
        border: 1px solid #FF8C00;
        border-radius: 10px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #FFA733;
        color: #101827;
        border-color: #FFA733;
    }

    /* Input fields */
    .stTextArea textarea {
        border: 2px solid #FF8C00;
        border-radius: 10px;
    }

    /* Highlighted results */
    [data-testid="stMetricValue"] {
        color: #FF8C00;
    }

    /* Links */
    a {
        color: #FFA733 !important;
    }
</style>
""", unsafe_allow_html=True)
,
)

st.markdown(
    """
    <div class="hero">
      <h1>🛡️ SpamBam</h1>
      <p>Your message's spam check, powered by Machine Learning.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

@st.cache_resource(show_spinner="Training SpamBam on the project dataset…")
def get_model():
    if not DATA_PATH.exists():
        return None, None, None
    frame = load_dataset(DATA_PATH)
    model = build_pipeline()
    model.fit(frame["data"], frame["label"])
    return model, len(frame), frame["label"].value_counts().to_dict()

model, row_count, label_counts = get_model()

if model is None:
    st.error("The dataset file is missing.")
    st.markdown(
        """
        **Expected file:** `Dataset/raw/SA_SubTxt_fn.csv`

        In VS Code, place the SpamAssassin CSV in that folder. Or open the VS Code terminal and run:

        ```bash
        python Python/download_dataset.py
        ```

        Then refresh this page.
        """
    )
    st.stop()

st.caption(f"Model ready • trained on {row_count:,} messages from the project dataset")

with st.form("spam_check_form"):
    message = st.text_area(
        "Paste an email or message",
        height=220,
        placeholder="Paste the subject and message body here…",
    )
    submitted = st.form_submit_button("Check message", type="primary", use_container_width=True)

if submitted:
    if not message.strip():
        st.warning("Please paste a message first.")
    else:
        prediction = int(model.predict([clean_text(message)])[0])
        probabilities = model.predict_proba([clean_text(message)])[0]
        classes = list(model.classes_)
        spam_probability = float(probabilities[classes.index(1)]) if 1 in classes else 0.0
        confidence = max(float(p) for p in probabilities) * 100

        st.divider()
        if prediction == 1:
            st.error("🚨 Likely SPAM")
            st.write("SpamBam found patterns that are more commonly associated with spam.")
        else:
            st.success("✅ Likely NOT SPAM (Ham)")
            st.write("SpamBam found patterns that are more commonly associated with legitimate messages.")

        st.metric("Estimated spam probability", f"{spam_probability * 100:.1f}%")
        st.progress(spam_probability)
        st.caption(f"Model confidence for its selected class: {confidence:.1f}%")

        st.info(
            "This is a machine-learning estimate, not a guarantee. Check suspicious links, "
            "sender addresses, and unexpected attachments carefully."
        )

with st.expander("About this project"):
    st.write(
        "SpamBam uses a Bag-of-Words text representation (CountVectorizer) and a "
        "Multinomial Naive Bayes classifier trained on the SpamAssassin public email corpus."
    )
    st.write("Labels: 0 = Ham (not spam), 1 = Spam.")

st.markdown(
    '<p class="small-note">Student AI project • Text classification • Python + Streamlit</p>',
    unsafe_allow_html=True,
)
