%%writefile /content/multimodal-rag-fastapi/src/models/embeddings.py
import hashlib
from typing import List


def _hash_embedding(text: str, dim: int = 128) -> List[float]:
    text = text or ""
    values = [0.0] * dim

    for token in text.lower().split():
        h = hashlib.md5(token.encode("utf-8")).hexdigest()
        idx = int(h[:8], 16) % dim
        sign = 1.0 if int(h[8:9], 16) % 2 == 0 else -1.0
        values[idx] += sign

    norm = sum(v * v for v in values) ** 0.5
    if norm > 0:
        values = [v / norm for v in values]

    return values


def get_document_embedding(text: str, model: str = "") -> list:
    return _hash_embedding(text)


def get_query_embedding(text: str, model: str = "") -> list:
    return _hash_embedding(text)