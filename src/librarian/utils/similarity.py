import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def similarity(vector_1: np.ndarray, vector_2: np.ndarray) -> float:
    """
    Computes the cosine similarity between two vectors.

    Args:
        vector_1 (np.ndarray): The first vector.
        vector_2 (np.ndarray): The second vector.

    Returns:
        float: The cosine similarity between the two vectors.
    """
    return cosine_similarity(vector_1.reshape(1, -1), vector_2.reshape(1, -1))[0][0]