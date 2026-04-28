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
# HEADER
# -------------------------------
st.title(" Real-Time Sentiment Analysis Dashboard")
st.markdown("Analyze stock & brand sentiment using live news + NLP")

# -------------------------------
# INPUT (MAIN AREA - CENTERED)
# -------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    query = st.text_input(" Enter stock or brand name")
    search = st.button("Analyze")

# -------------------------------
# SIDEBAR (INFO ONLY)
# -------------------------------
st.sidebar.title(" Dashboard Info")
st.sidebar.markdown("""
This dashboard analyzes sentiment from live news articles.

**How to use:**
1. Enter a stock or brand name  
2. Click Analyze  
3. View sentiment insights  
""")

# -------------------------------
# MAIN LOGIC
# -------------------------------
if search and query:

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
        fig1, ax1 = plt.subplots()
        sns.countplot(data=df, x="Sentiment", ax=ax1)
        st.pyplot(fig1)

    # Pie chart
    with col2:
        st.subheader("Sentiment Share")
        fig2, ax2 = plt.subplots()
        df["Sentiment"].value_counts().plot.pie(
            autopct="%1.1f%%",
            colors=["#4CAF50", "#FFC107", "#F44336"],
            ax=ax2
        )
        ax2.set_ylabel("")
        st.pyplot(fig2)

    # Line chart
    st.subheader("Sentiment Score Trend")
    st.line_chart(df["Score"])

    # Raw data
    st.subheader("Raw Data")
    st.dataframe(df)

elif search and not query:
    st.warning("Please enter a stock or brand name.")

else:
    st.info("Enter a stock or brand name and click Analyze to begin.")
