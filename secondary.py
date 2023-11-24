from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#FIRST STEP
#access the website
driver = webdriver.Chrome()
driver.get("https://www.pracuj.pl/")

#deal with popups
cookies = driver.find_element(By.CSS_SELECTOR, '[data-test="button-submitCookie"]')
cookies.click() #action.click(cookies)
print('button clicked')

#insert the info
search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'core_fhefgxl'))
)
search.click()
search.send_keys('data analyst')
print('Info inserted:', search.get_attribute('value'))

#click search button
search_button = driver.find_element(By.CLASS_NAME, 'size-large.variant-primary.core_b1fqykql')
search_button.click()
print('button clicked')

''#SECOND STEP
#gather is a list the websites
list_a_tags = driver.find_elements(By.CSS_SELECTOR, '[data-test="link-offer"]')
list_urls = [link.get_attribute("href") for link in list_a_tags]
print(list_urls)

'''#THIRD STREP
#make a loop that runs through the list_urls that will identify the requirements
for link in list_urls[:1]:
    driver.get(link)


time.sleep(30)
driver.quit()'''''

