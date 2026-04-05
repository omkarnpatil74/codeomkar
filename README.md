# Multimodal RAG FastAPI

## 📌 Overview
This project implements a **Multimodal Retrieval-Augmented Generation (RAG)** system using FastAPI.

It allows users to:
- Upload PDF documents
- Extract text, tables, and image summaries
- Perform semantic search
- Generate answers using retrieved context

---

## 🚀 Features
- PDF ingestion (text + tables + images)
- Vector search using ChromaDB
- FastAPI backend with endpoints:
  - `/health`
  - `/ingest`
  - `/query`
- Lightweight implementation for fast execution

---

## 🛠 Tech Stack
- Python
- FastAPI
- ChromaDB
- PDFPlumber
- Uvicorn

---

## 📂 Project Structure