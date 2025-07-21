import click

from rag import ingest, perform_rag_query


@click.group()
def cli():
    """Simple command-line interface."""
    pass


@cli.command()
@click.option('--url', required=True, help='URL to crawl')
def crawl_cmd(url):
    """Fetch and ingest a single URL."""
    ingest(url)
    click.echo(f'Ingested {url}')


@cli.command()
@click.option('--query', required=True, help='Query string')
def query(query):
    result = perform_rag_query(query)
    click.echo(result)


if __name__ == '__main__':
    cli()
