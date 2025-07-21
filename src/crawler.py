import urllib.request


def fetch_url(url: str) -> str:
    """Retrieve raw HTML content from a URL."""
    with urllib.request.urlopen(url) as response:
        return response.read().decode()


def crawl(urls):
    """Yield dictionaries with URL and HTML content."""
    for url in urls:
        try:
            html = fetch_url(url)
            yield {"url": url, "content": html}
        except Exception:
            # Skip URLs that fail to fetch
            continue
