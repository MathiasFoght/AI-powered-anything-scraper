# AI-Powered Web Scraper

This project turns web pages into useful data in seconds. 

Enter a URL, scrape the fully rendered page and ask an AI to extract exactly what you care about using natural-language instructions. 

## Features

- Scrapes dynamic websites with Selenium + Bright Data Scraping Browser
- Handles CAPTCHA flow
- Cleans DOM content by removing script/style noise
- Splits large pages into batches for LLM parsing
- Uses OpenAI GPT models via LangChain for prompt-driven extraction
- Simple Streamlit interface for end-to-end scrape and parse workflow

## Requirements

- Python 3.11+
- `uv` installed
- OpenAI API key
- Bright Data Scraping Browser endpoint

## Installation

```bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root (you can copy from `.env.example`):

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=your_openai_model
SBR_WEBDRIVER=your_bright_data_endpoint_for_selenium
```


## Run The App

```bash
.venv/bin/streamlit run main.py
```

Then open the URL in your terminal.

## How it Works

1. Enter a website URL.
2. Click `Scrape website`.
3. Describe what you want to extract in `Describe what you want to parse?`.
4. Click `Parse Content`.
5. The LLM will extract the information you asked for.


