
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

    driver = webdriver.Chrome(options=options, service=s)

    try:
        
        driver.get(url)
        wait = WebDriverWait(driver, 5)
        html = driver.page_source
    except Exception as ex:
        print(ex)
        html = None
    finally:
        driver.close()
        driver.quit()
    return html

html = get_html('https://www.wildberries.ru/catalog/23431872/detail.aspx')


