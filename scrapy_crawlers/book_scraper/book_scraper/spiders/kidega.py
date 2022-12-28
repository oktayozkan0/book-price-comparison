import scrapy

class KidegaBooksSpider(scrapy.Spider):
    name = 'kidega'
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"}


    def __init__(self, query, name=None, **kwargs):
        self.q = query

    def start_requests(self):
        yield scrapy.Request(f"https://kidega.com/arama/{self.q}/", headers=self.headers, callback=self.book_page)

    def book_page(self, response):
        books = response.xpath("//ul[@class='emosInfinite product-list-grid view-box']/li")
        for book in books[:10]:
            url = response.urljoin(book.xpath(".//a[@class='prd-lnk']/@href").get())
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)
    
    def parse(self, response):
        price = float((response.xpath("//span[@class='urunDetay_satisFiyat']/text()[1]").get() + response.xpath("//span[@class='urunDetay_satisFiyat']/span[@class='d']/text()").get()).replace(",","."))
        yield {
            "provider" : "KIDEGA",
            "title" : response.xpath("//div[@id='plhUrunAdi']/h1/text()").get(),
            "price" : f"{price:.2f}",
            "author" : response.xpath("//div[@id='plhUreticiKisaBilgi']/div/a/span/text()").get(),
            "product_url" : response.url,
            "image_url" : response.xpath("//li[@class='swiper-slide']/@data-large").get(),
            "publisher" : response.xpath("//span[@class='distributor-name']/text()").get(),
        }
