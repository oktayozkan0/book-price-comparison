import scrapy


class IdefixSpider(scrapy.Spider):
    name = 'idefix'
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"}


    def __init__(self, query, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.q = query

    def start_requests(self):
        yield scrapy.Request(f"https://www.idefix.com/Search?ActiveCategoryId=11693&MainCategoryId=0&Q={self.q}&redirect=search&Page=1", headers=self.headers, callback=self.book_page)
    
    def book_page(self, response):
        books = response.xpath("//div[@id='facetProducts']/div")
        for book in books[:10]:
            url = response.urljoin(book.xpath(".//div[@class='box-title']/a/@href").get())
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)
    
    def parse(self, response):
        price = float(response.xpath("//div[@id='salePrice']/text()").get().split(" ")[0].replace(",","."))
        yield {
            "provider" : "IDEFIX",
            "title" : response.xpath("//div[@class='prodyctDetailTopTitle']/h1/text()").get().strip(),
            "price" : f"{price:.2f}",
            "author" : response.xpath("(//a[@class='author-text'])[1]/text()").get(),
            "product_url" : response.url,
            "image_url" : response.xpath("//a[@class='showZoomable ImageZoom']/img/@data-src").get(),
            "publisher" : response.xpath("(//div[@class='publisher']/a/text())[1]").get(),
            }
