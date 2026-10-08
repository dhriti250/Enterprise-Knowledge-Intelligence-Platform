# Enterprise AI Knowledge Platform

A production-oriented Retrieval-Augmented Generation (RAG) platform for enterprise documents. The project is built incrementally, with independently replaceable components and evaluation as a first-class concern.

## Current phase: application foundation

The initial runtime foundation includes:

- A FastAPI application factory and ASGI entry point (`app.main:app`)
- Validated settings loaded from environment variables or a local `.env` file
- JSON-formatted application logs
- A liveness endpoint at `GET /health`
- Focused API foundation tests

The health endpoint reports process liveness only. It does not yet claim that databases, queues, or other dependencies are ready.

## Local development

Use Python 3.10 or newer. Create and activate a virtual environment, then install development dependencies:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

On macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Set configuration with environment variables or copy `.env.example` to `.env`. Available settings in this phase are `APP_NAME`, `ENVIRONMENT`, and `LOG_LEVEL`.

Run the tests with:

```bash
pytest
```

## Architecture roadmap

Planned phases include document ingestion and asynchronous processing, storage and embedding abstractions, hybrid retrieval and reranking, grounded answer generation with citations, evaluation, and operational integrations. Components will be introduced when their interfaces and behavior can be tested; unconfigured external services will not be represented by fake implementations.
