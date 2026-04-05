%%writefile multimodal-rag-fastapi/src/schemas.py
from typing import List, Optional
from pydantic import BaseModel, Field


class SourceReference(BaseModel):
    filename: str = Field(..., description="Source PDF filename")
    page: int = Field(..., description="Page number in source PDF")
    chunk_type: str = Field(..., description="Chunk type: text, table, or image")


class QueryRequest(BaseModel):
    question: str = Field(..., description="Natural language question")
    top_k: int = Field(3, ge=1, le=10, description="Number of chunks to retrieve")


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceReference]


class IngestResponse(BaseModel):
    filename: str
    text_chunks: int
    table_chunks: int
    image_chunks: int
    total_chunks: int
    processing_time_seconds: float


class HealthResponse(BaseModel):
    status: str
    model_readiness: str
    indexed_documents: int
    index_size: int
    uptime_seconds: float