import requests
import os
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime
from storage import load_articles, save_articles

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

def extract_keywords(text, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    X = vectorizer.fit_transform([text])
    scores = zip(vectorizer.get_feature_names_out(), X.toarray()[0])
    sorted_keywords = sorted(scores, key=lambda x: x[1], reverse=True)
    return [kw for kw, score in sorted_keywords[:top_n]]

def fetch_and_store_articles():
    print("Fetching articles...")
    url = f"{URL}{API_KEY}"
    res = requests.get(url)

    # res_json = res.json()
    # print(res_json)

    if res.status_code != 200:
        print("Failed to fetch articles:", res.status_code)
        return

    new_articles = []
    existing_articles = load_articles()
    existing_urls = {article["url"] for article in existing_articles}

    for article in res.json().get("articles", []):
        if article["url"] in existing_urls:
            continue

        content = article.get("description") or ""
        keywords = extract_keywords(content)

        new_articles.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "url": article["url"],
            "content": content,
            "published_at": article["publishedAt"],
            "keywords": ", ".join(keywords)
        })

    if new_articles:
        all_articles = new_articles + existing_articles
        save_articles(all_articles)
        print(f"Added {len(new_articles)} new articles.")
    else:
        print("No new articles found.")


fetch_and_store_articles()

