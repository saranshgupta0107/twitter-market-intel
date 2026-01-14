import re
import unicodedata

def normalize_text(text):
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    return text.lower().strip()








# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/