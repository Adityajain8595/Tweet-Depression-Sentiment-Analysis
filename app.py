import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup


# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Preprocessing function 
def preprocess_text(text):
    text = text.lower()
    text = re.sub('[^a-z A-Z 0-9-]+','',text)
    text = " ".join([y for y in text.split() if y not in stopwords.words('english')])
    text = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , str(text))
    text = BeautifulSoup(text, 'lxml').get_text()
    text = " ".join(text.split())
    return text

# Streamlit UI
st.set_page_config(page_title="Tweet Depression Detector")
st.title("Tweet Depression Sentiment Analysis")
st.write("Enter a tweet below and check if it shows signs of depression.")

# Input box
tweet_input = st.text_area("📝 Enter Tweet:", height=150)

# Prediction
if st.button("🔍 Analyze"):
    if tweet_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        clean_text = preprocess_text(tweet_input)
        vec_input = vectorizer.transform([clean_text])
        prediction = model.predict(vec_input)[0]

        if prediction == 1:
            st.error("😔 The tweet indicates signs of **depression**.")
        else:
            st.success("😊 The tweet does **not** indicate depression.")

st.markdown("---")
st.caption("Made by Aditya Jain")