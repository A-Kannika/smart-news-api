# smart-news-api
A lightweight FastAPI application that fetches real-time news from NewsAPI.org, extracts keywords using NLP, and serves them through filterable JSON endpoints, all without using a database.

## Features

- Fetches real-time articles from [NewsAPI.org](https://newsapi.org)
- Uses TF-IDF (from scikit-learn) to extract top keywords from article content
- Serves filterable articles via JSON API using FastAPI
- Automatically refreshes data every hour using APScheduler
- Stores data locally in a JSON file (no SQL or database required)
- Auto-generated interactive API docs via Swagger UI

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/news-aggregator-api.git
cd news-aggregator-api
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Your NewsAPI Key
Get your free key at https://newsapi.org.

Edit fetch_data.py:
```bash
NEWS_API_KEY = "YOUR_NEWSAPI_KEY"
```

### 4. Run the Server
Open your browser: http://127.0.0.1:8000/docs

```bash
uvicorn main:app --reload
```

## API Endpoints
GET /api/articles
Returns a list of stored articles.

Optional query parameters:
- source: filter by article source (case-insensitive)
- keyword: filter by keyword (from NLP)

Example:
```bash
/api/articles?source=bbc&keyword=ai
```

### Example Output
```bash
[
  {
    "title": "AI Breakthrough in Climate Research",
    "source": "BBC News",
    "url": "https://www.bbc.com/news/ai-climate",
    "content": "...",
    "published_at": "2025-07-15T12:00:00Z",
    "keywords": "climate, ai, research, data, model"
  }
]
```

