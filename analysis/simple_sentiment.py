BULLISH = {
    "buy", "bullish", "breakout", "long", "support",
    "upside", "strong", "positive"
}

BEARISH = {
    "sell", "bearish", "breakdown", "short", "resistance",
    "downside", "weak", "negative"
}

def sentiment_score(text):
    words = set(text.split())
    return len(words & BULLISH) - len(words & BEARISH)






# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/