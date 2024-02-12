from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def search_job(job_title):
    #FIRST STEP
    #access the website
    driver = webdriver.Chrome()
    driver.get("https://www.pracuj.pl/")

    #deal with popups
    cookies = driver.find_element(By.CSS_SELECTOR, '[data-test="button-submitCookie"]')
    cookies.click() #action.click(cookies)

    #insert the info
    search_bar = driver.find_element(By.CLASS_NAME, 'core_fhefgxl')
    search_bar.click()
    search_bar.send_keys(f'{job_title}')
    print('Info inserted:', search_bar.get_attribute('value'))

    #click search button
    search_button = driver.find_element(By.CLASS_NAME, 'size-large.variant-primary.core_b1fqykql')
    search_button.click()

    #get the current url
    search_page = driver.current_url
    return search_page


