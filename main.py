from selenium import webdriver
from bs4 import BeautifulSoup
import csv

counter = 1
print("Give me amazon link(after selecting category link): ")
primary_url = input('>')
print("Give me the link of the next page up to the equal (=) sign after the 'page':")
page_link = input('>')
url = f'{primary_url}'
fields = ['Product_Name', 'Price', 'Ratings', 'Link']
filename = "AmazonProducts.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    csvwriter.writeheader()

def Amazon_scrape(url):
    driver = webdriver.Chrome(
        executable_path='./driver/chromedriver.exe')
    # url = 'https://www.amazon.com/s?k=Nintendo+Switch+Games&rh=n%3A16227133011&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=VDJP9G7PTYSBNTYFPRZ1&pf_rd_s=merchandised-search-5&pf_rd_t=101&ref=nb_sb_noss'
    driver.get(url)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')

    infos = soup.find_all(
        'div', class_='a-section a-spacing-small a-spacing-top-small')

    for info in infos:
        product = info.find(
            'span', class_='a-size-medium a-color-base a-text-normal')
        price = info.find('span', class_='a-offscreen')
        ratings = info.find('span', class_='a-size-base s-underline-text')
        link = info.find(
            'a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal', href=True)
        
        if (product and price) and (ratings and link) is not None:
            print(f"Product name: {product.text}\n")
            print(f"Price: {price.text}\n")
            print(f"Ratings: {ratings.text}\n")
            url = link.get('href')
            print(f"Link: https://www.amazon.com{url}\n\n")

            dict = {'Product_Name': product.text, 'Price': price.text, 'Ratings': ratings.text.replace('(', '').replace(')', ''),
                    'Link': f"https://www.amazon.com{url}/"}
            fields = ['Product_Name', 'Price', 'Ratings', 'Link']
            with open(filename, 'a', encoding='utf-8', newline="") as csvfile:

                csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
                csvwriter.writerow(dict)
                
            


def url2(page_link):
    page_link = page_link.rsplit(' ', 1)[0]
    url = (f'{page_link}{counter}')
    print(f"Next Page Link: {url}\n")
    return url




print(f'We are scraping this URL: {url}\n')
Amazon_scrape(url)


if __name__ == '__main__':

    while True:
        counter += 1
        print(f'Counter is: {counter}')
        url = url2(page_link)
        print('\n\n\n')
        print(f'We are scraping this URL next: {url}\n')
        Amazon_scrape(url)

        
