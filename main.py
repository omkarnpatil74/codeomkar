
from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Multimodal RAG API",
    description="API for PDF ingestion and querying using RAG",
    version="1.0.0"
)

# include routes
app.include_router(router)


# optional root (helps avoid 'Not Found')
@app.get("/")
def root():
    return {"message": "Multimodal RAG API is running"}