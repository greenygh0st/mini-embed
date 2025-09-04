FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && pip install --no-cache-dir \
    flask \
    sentence-transformers \
    einops \
    curl

COPY embed_server.py .

HEALTHCHECK CMD curl -f http://localhost:5000/health || exit 1

EXPOSE 5000

CMD ["python", "embed_server.py"]
