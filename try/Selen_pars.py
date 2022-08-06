
from csv import writer
import csv
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup



DRIVE_PATH = "D:/chromedriver.exe"

def get_html(url):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    
    s = Service(executable_path = DRIVE_PATH)

    web_driver = webdriver.Chrome(options=options, service=s)

    try:
        
        web_driver.get(url)
        wait = WebDriverWait(web_driver, 5)
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card__wrapper")))

        html = web_driver.page_source
    except Exception as ex:
        print(ex)
        html = None
    finally:
        web_driver.close()
        web_driver.quit()
    return html

html = get_html('https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony')

# def parce_html (html):
soup = BeautifulSoup(html, 'html.parser')
cls = 'product-card j-card-item j-good-for-listing-event'
products = soup.find_all("div",{"class":"product-card__brand"})

products_list =[]

for product in products:
    #print(product.attrs)
    name = product.find("div",{"class":"product-card__brand-name"}).text
    price = product.find("div",{"class":"product-card__price j-cataloger-price"}).find("span",{"class":"price"}).text.encode('ascii',errors='ignore')#.find("ins",{"class":"lower-price"}).text.encode('ascii',errors='ignore')
    products_list.append([name, price])
    #print(price)

head = ["name","Price"]

with open("data.csv","w", newline='') as outFile:
    writer = csv.writer(outFile, delimiter=',')
    writer.writerow(head)
    for product in products_list:
        writer.writerow(product)
print('ggggg')

