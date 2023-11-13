import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.pracuj.pl/praca/programista-bi-warszawa-burakowska-14,oferta,1002964067")

print(driver.title)
time.sleep(5)
driver.quit()

