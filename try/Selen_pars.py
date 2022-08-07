
from ast import Break
from csv import writer
import csv
from types import NoneType
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

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
s = Service(executable_path = DRIVE_PATH)
web_driver = webdriver.Chrome(options=options, service=s)

def get_html(url):
    
    try:
        
        web_driver.get(url)
        wait = WebDriverWait(web_driver, 5)
        
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card__wrapper")))

        html = web_driver.page_source
    except Exception as ex:
        print(ex)
        html = None
        web_driver.close()
        web_driver.quit()
    # finally:
    #     web_driver.close()
    #     web_driver.quit()
    return html

def parce_html (html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
    
        products = soup.find_all("div",{"class":"product-card__brand"})

        products_list =[]

        for product in products:
            #print(product.attrs)
            name = product.find("div",{"class":"product-card__brand-name"}).text
            price = product.find(["ins","span"],{"class":"lower-price"}).text.encode('ascii',errors='ignore').decode()
            products_list.append([name, price])
        

        head = ["name","Price"]

        with open("data.csv","a", newline='') as outFile:
            writer = csv.writer(outFile, delimiter=',')
            writer.writerow(head)
            for product in products_list:
                writer.writerow(product)
    except Exception as ex:
        print("Failure parsing!")

i = 1
html = 0
while True:
    html = get_html(f'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page={i}')
    print(f'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page={i}')
    if html == None:
        Break()
    parce_html(html)
    i+=10

web_driver.close()
web_driver.quit()
print('ggggg')

