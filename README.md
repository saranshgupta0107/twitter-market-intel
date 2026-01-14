# Twitter/X Indian Market Intelligence System

- A real-time data collection and analysis system that scrapes Indian stock market
discussions from Twitter/X and converts text sentiment into quantitative trading signals.


## Features

- Selenium-based scraping (no paid APIs)
- Anti-bot & rate-limit aware
- Unicode-safe (Hindi / Hinglish / emojis)
- Parquet-based analytical storage
- TF-IDF + engagement-weighted signals
- Memory-efficient visualization


## Target Hashtags

- #nifty50 #sensex #banknifty #intraday


## Python Version Requirement

- This project requires Python 3.10 or 3.11.
- After installing Python 3.11, you must recreate the virtual environment:
  - deactivate
  - rm -rf venv
  - python3.11 -m venv venv


## Twitter Login Note

- This project uses an existing Chrome profile to persist Twitter login.
- Ensure you are logged into Twitter in Chrome and close Chrome before running.


## Browser requirement

- Ensure Chrome is installed and matches your ChromeDriver version.
- You are already signed in on Twitter/X.


## Fault Tolerance

- If Twitter/X returns an error page or infinite scroll stalls,
the scraper exits gracefully and continues downstream processing
with collected data.


## Scraping Limits
- To avoid Twitter/X rate limits and ensure balanced data collection,
a fixed tweet quota of 10 is enforced per keyword.


## Graceful Shutdown
- Press Ctrl+C or ENTER to stop scraping.
- The browser will close cleanly and partial data will be saved.


## Setup

- brew install python@3.11
- git clone https://github.com/saranshgupta0107/twitter-market-intel.git
- cd twitter-market-intel
- source venv/bin/activate
- python3.11 --version 
- pip install --upgrade pip
- pip install -r requirements.txt


## Run

- python main.py


## Output

- data/raw/ → raw scraped tweets
- data/processed/ → cleaned parquet files
- Console sentiment signals with confidence intervals


## Connect with me

- https://github.com/saranshgupta0107
- https://www.linkedin.com/in/saranshgupta0107/