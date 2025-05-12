# 🧠 Mini Embed Server

A lightweight, containerized embedding API that runs locally using [sentence-transformers](https://www.sbert.net/). Designed to power semantic search and retrieval-augmented generation (RAG) pipelines **without relying on OpenAI or external APIs**.

---

## 🚀 Features

- Runs locally via Flask + Docker
- Uses the `all-MiniLM-L6-v2` model (384-dim embeddings)
- Accepts text over HTTP and returns vector embeddings
- CPU-friendly — no GPU required
- Built-in request logging to STDOUT

---

## 📦 Requirements

- Docker
- Python (for local testing without Docker)

---

## 🔧 Quick Start

### ▶️ Build and run with Docker

```bash
docker build -t mini-embed-server .
docker run -d -p 5000:5000 --name mini-embed-server mini-embed-server
```

### 📡 Test the API

```bash
curl -X POST http://localhost:5000/embed \
     -H "Content-Type: application/json" \
     -d '{"text": "How do I reset my password?"}'
```

---

## 🔄 API

### `POST /embed`

**Request Body:**
```json
{
  "text": "Your input text goes here"
}
```

**Response:**
```json
{
  "embedding": [0.123, -0.456, ...]
}
```

---

## 🔍 Use Cases

- Semantic search with PGVector
- Local RAG pipelines
- Embedding indexing for internal documents
- Offline language understanding

---

## 🛠️ Configuration

By default, the server listens on:

```
Host: 0.0.0.0
Port: 5000
```

Edit `embed_server.py` to change the model or port.

---

## 🧪 Development (without Docker)

```bash
pip install flask sentence-transformers
python embed_server.py
```

---

## 📝 License

MIT or similar — use freely, modify as needed.

---

## ✨ Inspired By

- [sentence-transformers](https://github.com/UKPLab/sentence-transformers)
- OpenAI Embeddings — but free and local