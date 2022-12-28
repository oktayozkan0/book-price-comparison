import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"}


    def __init__(self, query, name=None, **kwargs):
        self.q = query


    def start_requests(self):
        yield scrapy.Request(f"https://www.amazon.com.tr/s?k={self.q}&i=stripbooks", callback=self.books, headers=self.headers)


    def books(self, response):
        books_xpath = response.xpath("//div[@data-component-type='s-search-result']")
        for book in books_xpath[:10]:
            url = response.urljoin(book.xpath(".//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']/@href").get())
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)


    def parse(self, response):
        try:
            title = response.xpath("//span[@id='productTitle']/text()").get().strip()
        except:
            title = "Belirtilmemiş"

        try:
            try:
                price = response.xpath("//span[@id='price']/text()").get().replace("\xa0"," ")
            except:
                price = response.xpath("//span[@class='a-size-base a-color-price a-color-price']/text()").get().replace("\xa0"," ").strip()
        except:
            price = response.xpath("//a[@class='a-size-mini a-link-normal']/text()[2]").get().replace("\xa0"," ").strip()
        
        try:
            author = response.xpath("(//span[@class='author notFaded']/a)[1]/text()").get()
        except:
            author = "Belirtilmemiş"

        try:
            publisher = response.xpath("//div[@id='rpi-attribute-book_details-publisher']/div[@class='a-section a-spacing-none a-text-center rpi-attribute-value']/span/text()").get()
        except:
            publisher = "Belirtilmemiş"
        image_url = ".".join(response.xpath("//img[@id='imgBlkFront']/@src").get().split(".")[:-2]) + ".jpg"

        yield {

            "provider" : "AMAZON",
            "title" : title.replace(" (Kapak Değişebilir)","").replace(" (Kapak değişebilir)",""),
            "price" : float(price.split(" ")[0].replace(",",".")),
            "author" : author,
            "product_url" : response.url.split("/ref=")[0],
            "image_url" : image_url,
            "publisher" : publisher,
        }
