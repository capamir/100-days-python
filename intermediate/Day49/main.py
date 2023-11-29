from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3726910930&f_AL=true&f_E=2&f_WT=2&geoId=101174742&keywords=Python%20Django%20Developer&location=Canada&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
ACCOUNT_EMAIL = 'amirhn.workmail@gmail.com'
ACCOUNT_PASSWORD = 'Amir&nikta'

chrome_driver_path = 'C:\Developement\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get(URL)
time.sleep(1)

sign_in_button = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
sign_in_button.click()

time.sleep(3)

username_field = driver.find_element(By.NAME, 'session_key')
username_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.NAME, 'session_password') 
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
while True:
    pass