#!/usr/bin/env python3
import sys
import urllib.request
import re
from html.parser import HTMLParser


class ParagraphParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.record = False
        self.text_parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"p", "title", "h1", "h2"}:
            self.record = True

    def handle_endtag(self, tag):
        if tag.lower() in {"p", "title", "h1", "h2"} and self.record:
            self.record = False
            self.text_parts.append("\n")

    def handle_data(self, data):
        if self.record:
            cleaned = data.strip()
            if cleaned:
                self.text_parts.append(cleaned + " ")


def fetch_url(url: str) -> str:
    """Retrieve the URL and return its body as text."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def clean_html(html: str) -> str:
    """Remove scripts/styles and collapse whitespace."""
    html = re.sub(r"<script.*?>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style.*?>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"\s+", " ", html)
    return html


def extract_text(html: str) -> str:
    parser = ParagraphParser()
    parser.feed(html)
    return "".join(parser.text_parts)


def summarize(text: str, sentences: int = 3) -> str:
    sentence_list = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(sentence_list[:sentences]).strip()


    try:
        html = fetch_url(url)
    except Exception as exc:
        return f"Failed to fetch URL: {exc}"
def summarize_url(url: str, sentences: int = 3) -> str:
    """Fetch the URL and return a short summary."""

def main(url: str):
    html = fetch_url(url)
    cleaned = clean_html(html)
    text = extract_text(cleaned)
    if not text:
        return "No text found on the page."
    return summarize(text, sentences)


def main(url: str):
    summary = summarize_url(url)
    print(summary)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawl_and_summarize.py <URL>")
        sys.exit(1)
    main(sys.argv[1])
