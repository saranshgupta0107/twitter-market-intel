import pandas as pd

df = pd.read_parquet("data/processed/market_tweets.parquet")
print(df.head())
print(len(df))
print(df["hashtag"].value_counts())





# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/