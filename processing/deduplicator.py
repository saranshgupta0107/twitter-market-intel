import hashlib

class Deduplicator:
    def __init__(self):
        self.seen = set()

    def is_new(self, text):
        h = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if h in self.seen:
            return False
        self.seen.add(h)
        return True





# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/