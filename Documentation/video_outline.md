# Video presentation outline (maximum 3 minutes)

**0:00–0:20 — Introduction**  
“Hello. My project is SpamBam, a spam email detector. It uses machine learning to classify a message as spam or not spam.”

**0:20–0:45 — Dataset and idea**  
“I used a labelled SpamAssassin email dataset. The message text is converted into numerical word-count features using the Bag-of-Words approach.”

**0:45–1:15 — Model**  
“I trained a Multinomial Naive Bayes classifier. The model learns patterns associated with spam and legitimate messages.”

**1:15–2:10 — Live demonstration**  
Show the SpamBam website. Paste one clearly legitimate sample and one obvious spam-like sample. Click Check message and explain the displayed prediction and estimated spam probability. Do not show private email content.

**2:10–2:40 — Evaluation**  
Show the Orange Test & Score result and confusion matrix. Mention that the Orange evaluation used stratified 5-fold cross-validation. State the recorded accuracy of 97.9%, along with other metrics if time permits.

**2:40–3:00 — Conclusion**  
“SpamBam demonstrates how NLP and machine learning can help identify unwanted messages. It is an assistive prediction tool, not a guarantee, so suspicious messages should still be checked carefully. Thank you.”
