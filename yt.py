from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome ayarları
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com")
driver.maximize_window()
wait = WebDriverWait(driver, 15)
# Çerez onayını kapat kısmı
try:
    kabul_buton = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//ytd-button-renderer[@id='button']/a/tp-yt-paper-button[contains(.,'Kabul ediyorum')]")
    ))
    kabul_buton.click()
    print("Çerez onayı kapatıldı.")
except:
    print("Çerez onayı çıkmadı veya bulunamadı.")

arama_kutusu = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
arama_kutusu.send_keys("Fenerbahçe marşı")
arama_kutusu.send_keys(Keys.RETURN)
# Sonuçların gelmesini bekle
wait.until(EC.presence_of_element_located((By.ID, "contents")))

# İlk videoyu clickable olana kadar bekle ve tıkla
ilk_video = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "(//ytd-video-renderer//a[@id='thumbnail'])[1]")
))
ilk_video.click()

time.sleep(5)

driver.quit()
