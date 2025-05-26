# 🧠 Tweet Depression Sentiment Analysis using NLP

## 📘 Overview

This project uses Natural Language Processing (NLP) to analyze tweets and classify them as **depressed** or **not depressed**. By evaluating the language people use on social media, we aim to predict signs of depression — a potentially life-saving application of AI in mental health.

The model is built using **TF-IDF vectorization**, **text preprocessing (NLTK)**, and **oversampling techniques** to handle class imbalance. The final classifier is a **Logistic Regression** model optimized for high recall and F1-score.


## 💡 Problem Statement

> *"Finding if a person is depressed from their use of words on social media can definitely help in the cure!"*

Social media platforms often reveal the emotional and mental state of users. By identifying depressive patterns in tweets, this project aims to contribute toward **early detection and intervention** in mental health.

---

## 📁 Dataset

- The dataset contains **labeled tweets**, each marked as either:
  - `1` → Depressed
  - `0` → Not Depressed

- Tweets are anonymized and collected with the intent of studying mental health through language usage.

---

## ⚙️ Key Features

- ✅ **Text Preprocessing with NLTK**: Tokenization, lowercasing, stopwords, special characters, urls, tags and additional spaces removal, punctuation stripping, lemmatization.
- ✅ **TF-IDF Vectorization**: Converts cleaned text into numerical feature vectors.
- ✅ **Imbalance Handling**: Applied **SMOTE** on the minority class to create synthetic samples for it.
- ✅ **Logistic Regression Classifier**: Trained to maximize F1-score and Recall.
- ✅ **Model Evaluation**: Accuracy, Precision, Recall, F1-Score, Confusion Matrix and Classification Report

---

## 📊 Results

| Metric      | Value |
|-------------|-------|
| Precision   | 0.98  |
| Recall      | 0.96  |
| F1 Score    | 0.97  |

> ⚠️ Note: All results are evaluated on the untouched original test set to ensure fair and unbiased performance metrics.

---

## 🛠️ Tech Stack

- Python 🐍
- NLTK (Natural Language Toolkit)
- Scikit-learn
- Imbalanced-learn (`imblearn`)
- Pandas, NumPy

---

## Streamlit Webapp Interface




## 🧪 How to Run

1. Clone this repository and install dependencies:
  
   >> git clone https://github.com/Adityajain8595/Tweet-Depression-Sentiment-Analysis
   
   >> pip install -r requirements.txt

2. Run Streamlit app:

   >> streamlit run app.py

   or Go to the link https://tweet-depression-detector.streamlit.app/

---


## 📌 Disclaimer
This project is intended for educational purposes only and is not a replacement for professional mental health services. If you or someone you know is struggling with mental health, please seek help from qualified professionals.

## 📬 Contact
Made by Aditya Jain

📧 Reach out: [meaditya1103@gmail.com]

🔗 LinkedIn: (https://www.linkedin.com/in/adityajain8595/)
