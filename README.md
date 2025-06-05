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
