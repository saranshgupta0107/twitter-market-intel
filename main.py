from scraper.browser import get_driver
from scraper.twitter_scraper import TwitterScraper
from processing.cleaner import normalize_text
from processing.deduplicator import Deduplicator
from processing.storage import save_parquet
from utils.shutdown import GracefulKiller
from analysis.simple_sentiment import sentiment_score
from analysis.visualization import plot_sentiment
import sys
import threading
import pandas as pd

HASHTAGS = ["nifty50", "sensex", "banknifty", "intraday"]

TWEETS_PER_KEYWORD = 20

def wait_for_enter(killer):
    input("↩️  Press ENTER to stop scraping gracefully...\n")
    killer.kill_now = True

def main():
    killer = GracefulKiller()
    threading.Thread(
        target=wait_for_enter,
        args=(killer,),
        daemon=True
    ).start()

    driver = None
    all_tweets = []

    try:
        driver = get_driver()
        scraper = TwitterScraper(driver)
        dedup = Deduplicator()

        for tag in HASHTAGS:
            if killer.kill_now:
                break

            print(f"\n🔍 Scraping #{tag}")

            scraper.search_hashtag(tag)
            tweets = scraper.scrape_tweets(
                target_count=TWEETS_PER_KEYWORD,
                killer=killer
            )

            print(f"✅ Collected {len(tweets)} tweets for #{tag}")

            for t in tweets:
                t["hashtag"] = tag
                t["clean_text"] = normalize_text(t["parsed_text"])
                if dedup.is_new(t["clean_text"]):
                    all_tweets.append(t)

    except Exception as e:
        print(f"⚠️ Fatal error: {e}")

    finally:
        print("\n💾 Saving collected data...")

        if all_tweets:
            df = pd.DataFrame(all_tweets)
            df["sentiment"] = df["clean_text"].apply(sentiment_score)

            print("\n📊 Sentiment Summary:")
            print(df.groupby("hashtag")["sentiment"].mean())

            plot_sentiment(df)

            save_parquet(df, "data/processed/market_tweets.parquet")
            print(f"✅ Saved {len(all_tweets)} tweets")

        if driver:
            print("🧹 Closing browser...")
            driver.quit()

        print("👋 Shutdown complete.")
        sys.exit(0)



if __name__ == "__main__":
    main()








# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/