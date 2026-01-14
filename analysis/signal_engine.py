import numpy as np

def compute_signal(vectors, engagements):
    weights = np.log1p(engagements)
    signal = vectors.mean(axis=0).A1 * weights.mean()
    confidence = np.std(signal) / np.sqrt(len(weights))
    return signal, confidence




# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/ 