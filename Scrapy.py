import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "pluralsight"
    start_urls = ['http://app.pluralsight.com/playlist/f6836e0a-b63d-4f70-95a7-6943bba9e061']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='pl']")
        for titles in titles:
            title = titles.select("a/text()").extract()
            link = titles.select("a/@href").extract()
            print title, link
