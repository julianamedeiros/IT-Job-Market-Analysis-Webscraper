from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


#FIRST STEP
#access the website
driver = webdriver.Chrome()
driver.get("https://www.pracuj.pl/")

#deal with cookie popups
driver.find_element(By.CSS_SELECTOR, '[data-test="button-submitCookie"]').click() 

#insert the info
search = driver.find_element(By.CSS_SELECTOR, '[data-test="input-field"]')
search.send_keys('data analyst warsaw')

#click search button
driver.find_element(By.CLASS_NAME, 'size-large.variant-primary.core_b1fqykql').click()


time.sleep(5)
driver.quit()

