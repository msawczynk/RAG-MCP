# Usage Guide

This document summarizes how to crawl a website and query the API.

## Crawling

Run the CLI crawler with:

```bash
python src/cli.py crawl --url https://example.com
```

## Querying

Send a POST request to the `/query` endpoint:

```bash
curl -X POST http://localhost:5000/query \
     -H 'Content-Type: application/json' \
     -d '{"query": "Your question"}'
```

The API returns a JSON response containing the generated answer.

