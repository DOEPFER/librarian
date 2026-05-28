import ollama

import numpy as np
import numpy.typing as npt

from librarian.core.settings import embedding_model_id


def generate_vector(prompt: str) -> npt.NDArray[np.float64]:
    return np.array(ollama.embeddings(model=embedding_model_id, prompt=prompt)['embedding'])