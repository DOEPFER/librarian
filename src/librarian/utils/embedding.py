"""
Utility module for generating vector embeddings.

This module provides a function to generate vector embeddings from text
using the configured embedding model via the Ollama library.
"""

import numpy as np
import numpy.typing as npt
import ollama

from librarian.core.settings import embedding_model_id


def generate_vector(prompt: str) -> npt.NDArray[np.float64]:
    """
    Generates a vector embedding for a given text prompt.

    Args:
        prompt (str): The input text to be converted into an embedding.

    Returns:
        npt.NDArray[np.float64]: A numpy array containing the vector embedding.
    """

    return np.array(
        ollama.embeddings(model=embedding_model_id, prompt=prompt)["embedding"]
    )
