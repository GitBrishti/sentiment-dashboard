import requests
import streamlit as st

# Get API key from Streamlit secrets
API_KEY = st.secrets["NEWS_API_KEY"]
def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=20&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
    except Exception:
        return []

    articles = []

    for article in data.get("articles", []):
        # Handle None values safely
        title = article.get("title") or ""
        description = article.get("description") or ""

        text = title + " " + description

        # Avoid empty strings
        if text.strip():
            articles.append(text)

    return articles
