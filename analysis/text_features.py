from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english",
    ngram_range=(1, 2)
)

def vectorize(texts):
    return vectorizer.fit_transform(texts)






# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/