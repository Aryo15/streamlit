import streamlit as st
from textblob import TextBlob

st.title("Sentiment Classifier")
st.write("Enter a sentence and I’ll tell you whether it’s positive, negative, or neutral.")

user_input = st.text_input("Your sentence")

if user_input:
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("Positive 😊")
    elif polarity < 0:
        st.error("Negative 😠")
    else:
        st.info("Neutral 😐")
