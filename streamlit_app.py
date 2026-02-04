import streamlit as st
import joblib
import re

st.set_page_config(page_title="Flipkart Review Sentiment", layout="centered")

st.title("🛒 Flipkart Review Sentiment Analysis")
st.write("Enter a product review to predict sentiment")

# -------------------------
# Text cleaning
# -------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -------------------------
# Load local model
# -------------------------
@st.cache_resource
def load_model():
    model = joblib.load("sentiment_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# -------------------------
# User input
# -------------------------
review = st.text_area("✍️ Paste your review here:")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        cleaned = clean_text(review)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.success("✅ Positive Review 😊")
        else:
            st.error("❌ Negative Review 😞")
