from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def search_job(job_name):
    #FIRST STEP
    #access the website
    driver = webdriver.Chrome()
    driver.get("https://www.pracuj.pl/")
    
    #maximize window, else does not work
    driver.maximize_window()

    #deal with popups
    cookies = driver.find_element(By.CSS_SELECTOR, '[data-test="button-submitCookie"]')
    cookies.click() #action.click(cookies)

    #deal with span
    span_element = driver.find_element(By.CSS_SELECTOR, 'span')
    driver.execute_script("arguments[0].onclick = null;", span_element)


    #insert the info
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input[data-test="input-field"]')
    search_bar.click()
    search_bar.send_keys(f'{job_name}')
    search_bar.send_keys(Keys.ENTER)




    #get the current url
    search_page = driver.current_url
    return search_page


