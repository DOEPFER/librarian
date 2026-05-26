import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def similarity(vector_1: np.ndarray, vector_2: np.ndarray) -> float:
    return cosine_similarity(vector_1.reshape(1, -1), vector_2.reshape(1, -1))[0][0]