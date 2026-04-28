import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sentiment import get_sentiment
from data_news import get_news

st.title(" Real-Time Sentiment Analysis Dashboard")
st.markdown("Analyze stock & brand sentiment using live news + NLP ")
st.sidebar.title(" Dashboard Controls")
st.sidebar.markdown("Enter any stock or brand name to analyze sentiment")

query = st.text_input("Enter stock or brand name")

if st.button("Analyze"):

    texts = get_news(query)
    st.success(f"Fetched {len(texts)} articles successfully ")

    results = []

    for text in texts:
        sentiment, score = get_sentiment(text)
        results.append([text, sentiment, score])

    df = pd.DataFrame(results, columns=["Text", "Sentiment", "Score"])
    if len(df) == 0:
       st.warning("No data found. Try another keyword.")
       st.stop()

    st.dataframe(df)

    # Chart 1
    st.subheader("Sentiment Distribution")
    fig1 = plt.figure()
    sns.countplot(x=df["Sentiment"])
    st.pyplot(fig1)

    # Chart 2
    st.subheader("Score Trend")
    fig2 = plt.figure()
    plt.plot(df["Score"])
    st.pyplot(fig2)