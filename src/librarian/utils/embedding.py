import ollama

import numpy as np
import numpy.typing as npt

def generate_vector(model: str, prompt: str) -> npt.NDArray[np.float64]:
    return np.array(ollama.embeddings(model=model, prompt=prompt)['embedding'])