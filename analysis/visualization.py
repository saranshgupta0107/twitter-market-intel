import matplotlib.pyplot as plt

def plot_sentiment(df):
    ax = df.groupby("hashtag")["sentiment"].mean().plot(
        kind="bar",
        title="Average Market Sentiment by Hashtag"
    )
    ax.set_ylabel("Sentiment Score")
    plt.tight_layout()
    plt.show()






# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/