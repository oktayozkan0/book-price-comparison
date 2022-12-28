import scrapy


class BkmSpider(scrapy.Spider):
    name = 'bkm' 

    def __init__(self, query, name=None, **kwargs):
        self.q = query

    def start_requests(self):
        yield scrapy.Request(f"https://bkm.wawlabs.com/avx_wse?cm=conv&f=True&d=True&q={self.q}", callback=self.parse)

    def parse(self, response):
        data = response.json()
        books = data["res"][:10]
        for book in books:
            price = float(book["Price_txt_tr"].replace(",",".")) - ((float(book["Price_txt_tr"].replace(",","."))) / 100) * float(book["Discount"])
            yield {
                "title": book["Title_txt_tr"],
                "author": book["Brand_txt_tr"],
                "price": f"{price:.2f}",
                "publisher": book["Publisher"],
                "image_url": book["Image_txt_tr"],
                "product_url": book["Link_txt_tr"],
                "provider": "BKM Kitap"
            }
