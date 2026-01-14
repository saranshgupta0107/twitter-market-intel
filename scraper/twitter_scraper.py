from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import random

class TwitterScraper:
    def __init__(self, driver, max_stall_scrolls=3):
        self.driver = driver
        self.max_stall_scrolls = max_stall_scrolls

    def search_hashtag(self, hashtag):
        url = f"https://twitter.com/search?q=%23{hashtag}&f=live"
        self.driver.get(url)
        time.sleep(random.uniform(4, 6))

    def scrape_tweets(self, target_count, killer=None):
        tweets = []
        seen_texts = set()
        stall_count = 0
        last_height = self._get_scroll_height()

        while len(tweets) < target_count:
            if killer and killer.kill_now:
                print("🛑 Stopping scrape due to user interrupt.")
                break
            try:
                if self._twitter_error_present():
                    print("⚠️ Twitter error detected. Stopping scrape.")
                    break

                cards = self.driver.find_elements(By.XPATH, '//article')

                for card in cards:
                    if len(tweets) >= target_count:
                        break

                    raw = card.text                    
                    text = self._clean_card_text(raw)

                    if not text:
                        continue

                    if text in seen_texts:
                        continue

                    seen_texts.add(text)
                    tweets.append({
                        "content": raw,
                        "parsed_text": text
                    })

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.uniform(2, 3))

                new_height = self._get_scroll_height()

                if new_height == last_height:
                    stall_count += 1
                    if stall_count >= self.max_stall_scrolls:
                        print("⚠️ Scroll stalled. Ending scrape early.")
                        break
                else:
                    stall_count = 0

                last_height = new_height

            except WebDriverException as e:
                print(f"⚠️ WebDriver exception: {e}")
                break
            except Exception as e:
                print(f"⚠️ Unexpected error: {e}")
                break

        return tweets

    def _get_scroll_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def _twitter_error_present(self):
        error_markers = [
            "Something went wrong",
            "Try reloading",
            "Retry"
        ]
        return any(m in self.driver.page_source for m in error_markers)

    def _clean_card_text(self, raw_text):
        lines = raw_text.split("\n")
        cleaned = []

        for line in lines:
            if line.startswith("@"):
                continue
            if "·" in line and "m" in line:
                continue
            cleaned.append(line)

        return " ".join(cleaned).strip()








# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/