from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

mau_apa = input("Apa yang ingin dicari? ")

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servis, options=opsi) 

url = f'https://www.tokopedia.com/search?st=&q={mau_apa}'
driver.set_window_size(1300, 800)
driver.get(url)

rentang = 600
for i in range(1, 7):
    akhir = rentang * i
    perintah = "window.scrollTo(0, " + str(akhir) + ")"
    driver.execute_script(perintah) 
    print("Scroll ke " + str(akhir))
    time.sleep(1)

time.sleep(5)
driver.save_screenshot('home.png')
konten = driver.page_source
driver.quit()

soup = BeautifulSoup(konten, 'html.parser')

i = 1

base_url = 'https://www.tokopedia.com'

list_nama, list_gambar, list_harga, list_link, list_terjual, list_lokasi = [], [], [], [], [], []

for area in soup.find_all('div', class_="css-rjanld"):
    print("Memproses data ke - " + str(i))
    nama = area.find('div',class_="ie3A+n bM+7UW Cve6sh").get_text()
    gambar = area.find('img')['src']
    harga = area.find('span',class_="ZEgDH9").get_text()
    link = base_url + area.find('a')['href']
    terjual = area.find('div',class_="r6HknA uEPGHT")
    if terjual != None:
        terjual = terjual.get_text()
    lokasi = area.find('div',class_="zGGwiV").get_text()

    list_nama.append(nama)
    list_gambar.append(gambar)
    list_harga.append(harga)
    list_link.append(link)
    list_terjual.append(terjual)
    i+=1
    print("------")

df = pd.DataFrame({
    'Nama': list_nama,
    'Gambar': list_gambar,
    'Harga': list_harga,
    'Link': list_link,
    'Terkini': list_terjual,
    'Lokasi': list_lokasi})

tulis = pd.ExcelWriter(f"E:\\Coding\\Python\\shopee\\newww\\{mau_apa}.xlsx")
df.to_excel(excel_writer=tulis, sheet_name="Tokopedia_1", index=False)
tulis.close()

print(f"File '{mau_apa}.xlsx' created successfully.")

input("Tekan 'Enter' untuk keluar...")