from typing import Dict
import urllib.request

from parser import parse_html_content


documents: Dict[str, str] = {}


def ingest(url: str) -> None:
    """Fetch a URL and store its parsed text."""
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
    text = parse_html_content(html)
    documents[url] = text


def perform_rag_query(query: str) -> str:
    """Return a simple match from ingested documents."""
    for url, text in documents.items():
        if query.lower() in text.lower():
            snippet = text[:200].replace("\n", " ")
            return f"From {url}: {snippet}"
    return "No results found."
