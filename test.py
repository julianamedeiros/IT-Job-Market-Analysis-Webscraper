from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def scan_requirements(website):
    driver = webdriver.Chrome()
    driver.get(website)
    print(driver.title)

    #deal with popups
    
    requirements = driver.find_element(By.CLASS_NAME, 'offer-viewU0gxPf')
    print(requirements)
    time.sleep(10)
    driver.quit()

scan_requirements("https://www.pracuj.pl/praca/data-scientist-warszawa,oferta,1002985977")

