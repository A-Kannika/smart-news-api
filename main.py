from fastapi import FastAPI, Query
from storage import load_articles
from fetch_data import fetch_and_store_articles
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

@app.on_event("startup")
def startup_event():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_store_articles, 'interval', hours=1)
    scheduler.start()
    fetch_and_store_articles()  # Fetch once at startup

@app.get("/api/articles")
def get_articles(source: str = Query(None), keyword: str = Query(None)):
    articles = load_articles()
    filtered = []

    for article in articles:
        if source and source.lower() not in article["source"].lower():
            continue
        if keyword and keyword.lower() not in article["keywords"].lower():
            continue
        filtered.append(article)

    return filtered
