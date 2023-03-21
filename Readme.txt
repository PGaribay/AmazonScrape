AmazonScraper

This app has two types for two different tabular display of products on Amazon website.
Use main.py for pages that display products in only one column.
Otherwise, use mainV2 (pages that display products in a tabular form with rows).
You can try to use the example URL's on step2 of main.py and mainV2.py to see the two type of tabular display of products.

Note:
No need to install the chromedriver for running this app. Selenium webdriver module will be the one to execute it.


Sample for main.py:
1. Open main.py file

2. Terminal window will prompt you (needs an input URL from the amazon website):
Give me amazon link(after selecting category link):
>https://www.amazon.com/s?k=nintendo&i=videogames-intl-ship&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=40T5FQJJFBK0B01YB620&pf_rd_s=merchandised-search-5&pf_rd_t=101&ref=nb_sb_noss

3. Another input needed but this time you have to click for the next page of the chosen category.
Give me the link of the next page up to the equal (=) sign after the 'page':
>https://www.amazon.com/s?k=nintendo&i=videogames-intl-ship&page=

4. The output is a csv file with default file name of "AmazonProducts.csv" that shows the Product's Name, Price, Ratings and Link.


Sample for mainV2.py:
1. Open mainV2.py file

2. Terminal window will prompt you (needs an input URL from the amazon website):
Give me amazon link(after selecting category link):
>https://www.amazon.com/s?i=specialty-aps&bbn=16225006011&rh=n%3A%2116225006011%2Cn%3A3777891&pd_rd_r=7b5a27dd-33e1-41a4-95d4-9e513fe81d63&pd_rd_w=wMbBR&pd_rd_wg=iEJLo&pf_rd_p=eab778f7-37cf-4c6b-9552-5370900592a9&pf_rd_r=8C2X0B151PH6MHV51BM7&ref=pd_gw_unk

3. Another input needed but this time you have to click for the next page of the chosen category.
Give me the link of the next page up to the equal (=) sign after the 'page':
>https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A3777891&page=

4. The output is a csv file with default file name of "AmazonProducts.csv" that shows the Product's Name, Price, Ratings and Link.