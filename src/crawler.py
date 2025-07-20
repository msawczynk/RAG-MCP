import scrapy
from scrapy_playwright.page import PageMethod

class HybridSpider(scrapy.Spider):
    name = 'hybrid'
    start_urls = ['https://example.com']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod('wait_for_selector', 'body')
                ]
            ))

    async def parse(self, response):
        # Parse logic here
        page = response.meta['playwright_page']
        content = await page.content()
        await page.close()
        # Process content
        yield {'url': response.url, 'content': content} 