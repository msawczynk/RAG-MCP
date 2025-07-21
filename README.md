# Self-Hosted Website Ingestion & Citation Service

## Overview

This is an open-source, self-hosted tool that crawls websites, indexes their content using advanced RAG techniques, and provides a retrieval API for querying with verifiable citations. It is designed for technical hobbyists, researchers, and small teams who need trustworthy, private knowledge bases.

Key Features (v1.0):
- Simple HTTP crawler using the standard library
- Basic HTML parsing with Python's `html.parser`
- Minimal in-memory retrieval pipeline
- FastAPI service exposing a `/query` endpoint
- Optional React dashboard

## Installation

### Prerequisites
- Docker and Docker Compose
- Python 3.10+
- Node.js for the UI

### Quick Start
1. Clone the repository: `git clone https://github.com/your-org/rag-mcp.git`
2. Navigate to the project: `cd rag-mcp`
3. Install dependencies: `pip install -r src/requirements.txt`
4. Crawl a site: `python src/cli.py crawl --url https://example.com`
5. Start the API: `python src/app.py`

For detailed setup, see [docs/installation.md](docs/installation.md).

## Usage

- Crawl a site: `python src/cli.py crawl --url https://example.com`
- Query the API: `curl -X POST http://localhost:5000/query -d '{\"query\": \"Your question\"}'`

For full documentation, see [docs/usage.md](docs/usage.md).

## Tiers and Licensing
- **Community**: Free, AGPLv3, limited to 2 websites.
- **Pro**: Subscription, unlimited, additional features.
See [Pricing](#pricing) for details.

## Contributing
Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the AGPLv3 - see the [LICENSE](LICENSE) file for details.