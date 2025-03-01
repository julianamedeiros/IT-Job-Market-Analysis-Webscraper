from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_job(job_name):
    # Access the website
    driver = webdriver.Chrome()
    driver.get("https://www.pracuj.pl/")
    
    # Maximize window, else does not work
    driver.maximize_window()

    # Deal with popups
    cookies = driver.find_element(By.CLASS_NAME, "popup_p1c6glb0")
    cookies.click() #action.click(cookies)

    cookies = driver.find_element(By.CSS_SELECTOR, '[data-test="button-submitCookie"]')
    cookies.click() #action.click(cookies)

    # Insert the job title
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input[data-test="input-field"]')
    search_bar.click()
    search_bar.send_keys(f'{job_name}')
    search_bar.send_keys(Keys.ENTER)

    # Get the current url
    search_page = driver.current_url
    return search_page


