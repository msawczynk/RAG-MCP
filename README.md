# Self-Hosted Website Ingestion & Citation Service

## Overview

This is an open-source, self-hosted tool that crawls websites, indexes their content using advanced RAG techniques, and provides a retrieval API for querying with verifiable citations. It is designed for technical hobbyists, researchers, and small teams who need trustworthy, private knowledge bases.

Key Features (v1.0):
- Hybrid crawling with Scrapy and Playwright
- Structure-aware parsing with Unstructured.io
- Advanced RAG pipeline: Semantic chunking, Parent Document Retrieval, hybrid search, re-ranking, and citation verification
- Vector storage with Qdrant (Pro) or ChromaDB (Community)
- React dashboard for monitoring and configuration
- REST API for queries

## Installation

### Prerequisites
- Docker and Docker Compose
- Python 3.10+
- Node.js for the UI

### Quick Start
1. Clone the repository: `git clone https://github.com/your-org/rag-mcp.git`
2. Navigate to the project: `cd rag-mcp`
3. Start the stack: `docker-compose up -d`
4. Access the dashboard at `http://localhost:3000`

For detailed setup, see [docs/installation.md](docs/installation.md).

## Usage

- Configure crawls via the dashboard or CLI: `python src/cli.py crawl --url https://example.com`
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