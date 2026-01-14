## Twitter/X Indian Market Intelligence System

A real-time market intelligence pipeline that scrapes Indian stock market discussions from Twitter/X and converts unstructured text into quantitative sentiment signals suitable for algorithmic trading research.

This project emphasizes fault tolerance, scalability, and production-ready design under real-world platform constraints.


## Key Features

- Selenium-based scraping
- Session-persistent Twitter/X login via Chrome profile
- Anti-bot & rate-limit aware scraping strategy
- Unicode-safe text handling (Hindi / Hinglish / emojis)
- Data deduplication and normalization
- Columnar storage using Parquet for analytics
- Lightweight NLP-based sentiment signal extraction
- Memory-efficient visualizations
- Graceful shutdown and partial data persistence


## Target Market Hashtags

- #nifty50
- #sensex
- #banknifty
- #intraday

These represent high-liquidity Indian indices commonly discussed by traders and analysts.


## System Architecture

Twitter/X (Live DOM)
        ↓
Selenium Scraper
        ↓
Text Cleaning & Deduplication
        ↓
Feature Engineering (NLP)
        ↓
Signal Aggregation
        ↓
Parquet Storage + Visualization


## Python Version Requirement

- Python 3.10 or 3.11 is required
- Python 3.12+ is not supported due to Selenium dependencies
- After installing Python 3.11, recreate the virtual environment:
  - deactivate
  - rm -rf venv
  - python3.11 -m venv venv
  - source venv/bin/activate


## Twitter/X Login & Browser Configuration

- The scraper reuses an existing Chrome profile to maintain login state
- Ensure:
  - You are logged into Twitter/X in Chrome
  - All Chrome windows are closed before running the script

This avoids repeated logins and reduces bot detection


## Fault Tolerance & Reliability

- Detects stalled infinite scrolling
- Detects Twitter/X error pages (e.g. “Something went wrong”)
- Automatically exits scraping loops on failure
- Continues downstream processing with already collected data
- Ensures browser shutdown even on interruption


## Scraping Limits & Rate Control

- A fixed tweet quota per hashtag is enforced (default: 20)
- Prevents over-scraping a single query
- Ensures balanced data collection across all market segments
- Limits are configurable for larger batch runs


## Graceful Shutdown

- Press ENTER or Ctrl+C to stop scraping at any time
- Browser closes cleanly
- Partial data is saved automatically
- No orphan Chrome processes


## Setup Instructions

- brew install python@3.11
- git clone https://github.com/saranshgupta0107/twitter-market-intel.git
- cd twitter-market-intel
- python3.11 -m venv venv
- source venv/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt

Verify:
- python --version


## Run the Pipeline

- python main.py


## Output Artifacts

- data/processed/ → cleaned and deduplicated Parquet files
- Console output:
  - Average sentiment scores per hashtag
  - Market bias visualization


## Sample Results

- With limited real-time samples, most market hashtags exhibit neutral sentiment, while occasional bullish or bearish bias appears depending on prevailing news flow.

- This reflects realistic market noise and avoids forced signals.


## Limitations & Future Improvements

- Twitter/X DOM structure is subject to change
- Sentiment model is rule-based for interpretability
- Larger datasets would benefit from transformer-based embeddings
- Engagement-weighted signals can be extended further


## Author

- Saransh Gupta
- GitHub: https://github.com/saranshgupta0107
- LinkedIn: https://www.linkedin.com/in/saranshgupta0107/


## Final Note

- This repository demonstrates real-world data engineering under constraints, emphasizing robustness, clarity, and scalability over naive scraping.