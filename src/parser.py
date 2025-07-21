from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.parts.append(text)


def parse_html_content(html_content: str) -> str:
    """Extract visible text from raw HTML."""
    extractor = TextExtractor()
    extractor.feed(html_content)
    return " ".join(extractor.parts)
