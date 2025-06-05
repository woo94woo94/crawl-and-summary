# crawl-and-summary

This small project provides a simple script that fetches a web page and prints a short summary of its content.

## Requirements

No external Python packages are required. The script relies only on the standard library.

## Usage

```bash
python crawl_and_summarize.py <URL>
```

The script downloads the specified URL, extracts text from `<p>` tags, and prints the first few sentences.

> **Note**: Internet access is required for the script to fetch external pages. On systems without internet connectivity the script will fail to retrieve the content.
