from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#access the website
driver = webdriver.Chrome()
driver.get("https://www.pracuj.pl/")

#deal with popups
cookies = driver.find_element(By.CSS_SELECTOR, '[data-test="button-submitCookie"]')
cookies.click()
print('button clicked')

#insert the info
search = driver.find_element(By.CLASS_NAME, 'core_fhefgxl')
search.send_keys('data analyst warsaw')
print('info inserted')
search.button = driver.find_element(By.CLASS_NAME, 'core_b1fqykql')
search.button.click()
print('button clicked')




time.sleep(10)
driver.quit()

