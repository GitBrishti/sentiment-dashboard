import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sentiment import get_sentiment
from data_news import get_news

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

# -------------------------------
# UI HEADER
# -------------------------------
st.title("📊 Real-Time Sentiment Analysis Dashboard")
st.markdown("Analyze stock & brand sentiment using live news + NLP 🚀")

st.sidebar.title("📊 Dashboard Controls")
query = st.sidebar.text_input("Enter stock or brand name")

# -------------------------------
# MAIN LOGIC
# -------------------------------
if query:

    # Fetch news
    texts = get_news(query)

    # Handle no data
    if not texts:
        st.error("No news found for this keyword. Try another stock or brand.")
        st.stop()

    st.success(f"Fetched {len(texts)} articles successfully 🚀")

    # Sentiment analysis
    results = []
    for text in texts:
        sentiment, score = get_sentiment(text)
        results.append([text, sentiment, score])

    # Create dataframe
    df = pd.DataFrame(results, columns=["Text", "Sentiment", "Score"])

    # -------------------------------
    # VISUALIZATION
    # -------------------------------

    col1, col2 = st.columns(2)

    # Bar chart
    with col1:
        st.subheader("Sentiment Distribution")
        sns.countplot(data=df, x="Sentiment")
        st.pyplot(plt)

    # Pie chart
    with col2:
        st.subheader("Sentiment Share")
        df["Sentiment"].value_counts().plot.pie(autopct="%1.1f%%")
        st.pyplot(plt)

    # Line chart
    st.subheader("Sentiment Score Trend")
    st.line_chart(df["Score"])

    # Show data
    st.subheader("Raw Data")
    st.dataframe(df)

else:
    st.info("Enter a stock or brand name in the sidebar to begin analysis.")
