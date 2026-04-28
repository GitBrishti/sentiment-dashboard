import requests

API_KEY = "1f110320d93749fc9f88d2817b46d4c2"

def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=20&apiKey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data.get("articles", []):
        text = article.get("title", "") + " " + article.get("description", "")
        articles.append(text)

    return articles