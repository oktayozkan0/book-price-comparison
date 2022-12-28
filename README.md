<br/>
<h2>Important note</h2>
This is an experimental project. There may be problems, bugs and prices might be wrong (they are usually true).
<h1> book-price-comparison </h1>
Simple Web Scraper with Django and Scrapy,
Only Turkish books and Turkish book eCommerce websites  (except Amazon)
<br/>
<br/>
Installation

for Windows:
```
pip install scrapy scrapyrt django 
```
for Linux:
```
pip3 install scrapy scrapyrt django 
```

Start ScrapyRT HTTP API

Open terminal in scrapy_crawlers/book_scraper and then:
```
scrapyrt
```

after run the scrapyrt successfully, run django server
<br/>
open terminal in price_comp/price_comp and then:
```
python manage.py runserver
```

after that, go to http://127.0.0.1:8000 in your browser and try search a book
<br/>
I will search "Satranç" which is Turkish translation of Stefan Zweig's The Royal Game
![image](https://user-images.githubusercontent.com/103560387/209805326-59c14eb5-8dd2-462b-a5dc-6fd1079b3b62.png)

and here is the results:
![image](https://user-images.githubusercontent.com/103560387/209805512-31cdc21c-3f27-45d0-8234-51f070ce77a3.png)
results are sorting by low to high price
<br/>
columns are BOOK TITLE, AUTHOR, PUBLISHER, PROVIDER, PRICE and	WEBSITE.
<br/>
By the way, you can go to website with GO button.
![image](https://user-images.githubusercontent.com/103560387/209805903-74d45319-b1ab-4f43-a513-589a9670e433.png)
![image](https://user-images.githubusercontent.com/103560387/209805934-6e46a2f3-fd74-4dd3-b24f-a983fb48db7f.png)






