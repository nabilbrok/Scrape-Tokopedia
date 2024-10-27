from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time


url = f'https://www.tokopedia.com/search?st=&q=handphone&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

for item in soup.findAll('div', class_="css-5wh65g"):
    try:
        nama_produk = item.find('div',class_="VKNwBTYQmj8+cxNrCQBD6g==").text
        harga_produk = item.find('div',class_="ELhJqP-Bfiud3i5eBR8NWg==").text
        lokasi = item.find('div',class_="_4iyO0jMqM71An9gZaTzQig==").text
        print(nama_produk)
        print(harga_produk)
        print(lokasi)
    except AttributeError:
        continue
        
    
    






driver.close()