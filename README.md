# crawl-and-summary

This small project provides a simple script that fetches a web page and prints a short summary of its content. It also includes a lightweight web service with a React UI.

## Requirements

The summarizer itself relies only on the Python standard library. Running the optional web service requires the `Flask` package.

## Usage

```bash
python crawl_and_summarize.py <URL>
```

The script downloads the specified URL, extracts text from `<p>` tags, and prints the first few sentences.

> **Note**: Internet access is required for the script to fetch external pages. On systems without internet connectivity the script will fail to retrieve the content.

## Web service

Install Flask and run `app.py` to start a small web server with a React interface:

```bash
pip install Flask
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser and enter a URL to generate a summary.
