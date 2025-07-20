import click
from crawler import HybridSpider
from scrapy.crawler import CrawlerProcess

@click.group()
def cli():
    pass

@cli.command()
@click.option('--url', required=True)
def crawl(url):
    process = CrawlerProcess(settings={
        'PLAYWRIGHT_BROWSER_TYPE': 'chromium',
    })
    process.crawl(HybridSpider, start_urls=[url])
    process.start()

@cli.command()
@click.option('--query', required=True)
def query(query):
    from rag import perform_rag_query
    result = perform_rag_query(query)
    print(result)

if __name__ == '__main__':
    cli() 