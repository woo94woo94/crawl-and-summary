# crawl-and-summary

This small project provides a simple script that fetches a web page and prints a short summary of its content. It also includes a lightweight web service with a React UI.

## Requirements

The crawler is implemented with the Python standard library. Summarization uses the OpenAI API, so you'll need an API key and the `openai` package installed. The optional web service also requires the `Flask` package.

Install the dependencies with:

```bash
pip install openai Flask
```

## Usage

```bash
python crawl_and_summarize.py <URL>
```

Set the `OPENAI_API_KEY` environment variable before running the script so it can
use the OpenAI API for summarization:

```bash
export OPENAI_API_KEY=your-key-here
```

The script downloads the specified URL, extracts text from the title and paragraphs, and prints the first few sentences. A browser-like `User-Agent` header is sent to avoid simple blocks.

> **Note**: Internet access is required for the script to fetch external pages. On systems without internet connectivity the script will fail to retrieve the content.

## Web service

Run `app.py` to start a small web server with a React interface:

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser and enter a URL to generate a summary.
