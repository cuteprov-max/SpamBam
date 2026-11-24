# SpamBam — Project Documentation

## Cover page
**Project:** SpamBam — Spam Email Detector  
**Subject:** Artificial Intelligence (Subject Code 843)  
**Student:** ____________________  
**Class / Section:** ____________________  
**Roll Number:** ____________________  
**School:** ____________________  
**Session:** 2026–27  
**Teacher / Guide:** ____________________

## 1. Introduction
Email and messaging services are widely used for communication. Unwanted messages may contain advertisements, misleading claims, or suspicious links. SpamBam is a text-classification project that predicts whether a message is spam or legitimate (ham).

## 2. Problem statement
Manually checking every incoming message is time-consuming. The project explores how machine learning can classify message text and assist users in identifying likely spam.

## 3. Objectives
- Understand a real-world text-classification problem.
- Prepare and inspect a labelled email dataset.
- Convert text into numerical features.
- Train a Naive Bayes classifier.
- Evaluate the model using standard classification metrics.
- Build a simple website to demonstrate predictions.
- Compare a Python implementation with an Orange Data Mining workflow.

## 4. AI concepts used
**Natural Language Processing (NLP):** techniques used to process and analyse human language.

**Tokenisation:** splitting text into smaller units such as words.

**Bag of Words:** representing a message using word-occurrence counts.

**Classification:** assigning an input to a predefined category.

**Naive Bayes:** a probabilistic classifier based on Bayes' theorem and a simplifying conditional-independence assumption.

## 5. Dataset
The project uses a SpamAssassin public email corpus CSV hosted in the `bvk/SpamAssassin-spam` Hugging Face dataset repository. The working copy used in the earlier analysis contained 6,046 messages: 4,150 ham and 1,896 spam.

Fields:
- `label`: target class (0 = ham, 1 = spam)
- `data`: message text
- `filename`: message identifier

The model uses `data` as its text input and `label` as the target. `filename` is retained as metadata and excluded from text features.

## 6. Methodology
1. Load the CSV using Pandas.
2. Inspect columns and class labels.
3. Remove unusable rows and convert message values to text.
4. Split the data into training and testing subsets for Python evaluation.
5. Convert messages into Bag-of-Words features using CountVectorizer.
6. Train a Multinomial Naive Bayes classifier.
7. Evaluate predictions using accuracy, precision, recall, F1-score, and a confusion matrix.
8. Build the Streamlit interface to accept a message and display the predicted class.

## 7. Python implementation
The complete runnable implementation is in the `Python/` folder:
- `download_dataset.py`
- `spam_model.py`
- `train_model.py`

The web interface is in the root file `app.py`. Run instructions are in the root README.

## 8. Orange implementation
The Orange workflow uses File, Select Columns, Corpus, Preprocess Text, Bag of Words, Naive Bayes, Test & Score, and Confusion Matrix. The exact field configuration and workflow are documented in `Orange/README.md`.

## 9. Results and evaluation
### Orange
The recorded stratified 5-fold cross-validation results were:
- AUC: 0.995
- Accuracy: 97.9%
- Precision: 98.9%
- Recall: 98.0%
- F1-score: 98.5%
- MCC: 0.951

The confusion matrix is included in `Results/README.md`.

### Python
The Python hold-out test is a separate evaluation. Run `python Python/train_model.py` and copy the fresh printed metrics into the practical record. The previously recorded confusion matrix is included in `Results/python_confusion_matrix.txt`.

## 10. Applications
- Filtering unwanted email.
- Flagging suspicious messages for review.
- Demonstrating NLP and supervised machine learning.
- Learning how text features can be used by classification algorithms.

## 11. Limitations
- A message can be misclassified.
- New spam patterns may differ from the training data.
- The model does not verify whether a link or sender is safe.
- Short or ambiguous messages may not contain enough useful text.
- The dataset may not represent every language, region, or current spam style.

## 12. Future scope
- Add more recent and diverse labelled messages.
- Compare Naive Bayes with other classifiers.
- Add subject-line and sender-related features where appropriate.
- Evaluate performance on a separate, newly collected dataset.
- Improve the interface and add batch testing.

## 13. Conclusion
SpamBam demonstrates an end-to-end text-classification workflow, from labelled data and feature extraction to model evaluation and a working web interface. The project shows how NLP and machine learning can help identify likely spam while recognising that predictions require human judgement.

## 14. Bibliography
1. CBSE, Artificial Intelligence Student Handbook, Class XII, Subject Code 843.
2. Hugging Face dataset repository: `bvk/SpamAssassin-spam`.
3. Python documentation: https://docs.python.org/3/
4. scikit-learn documentation: https://scikit-learn.org/stable/
5. Streamlit documentation: https://docs.streamlit.io/
6. Orange Data Mining documentation: https://orangedatamining.com/
