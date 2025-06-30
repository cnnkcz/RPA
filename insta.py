from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome ayarları
options = webdriver.ChromeOptions()
# options.add_argument("--incognito")-gizli mod ayarı

driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()#sayfa boyutlaması

time.sleep(5)

kullanici_adi_kutusu = driver.find_element(By.NAME, "username")
kullanici_adi_kutusu.send_keys("cnnkcz")

sifre_kutusu = driver.find_element(By.NAME, "password")
sifre_kutusu.send_keys("Cnn7kcz+")

time.sleep(3)

sifre_kutusu.send_keys(Keys.RETURN)

time.sleep(5)

# Eğer "Bildirimleri Aç" penceresi çıkarsa diye try catch bloğu denemesi
try:
    bildirimleri_sonra = driver.find_element(By.XPATH, "//button[contains(text(), 'Şimdi Değil')]")
    bildirimleri_sonra.click()
except:
    pass

time.sleep(5)

# Tarayıcıyı kapat
driver.quit()
