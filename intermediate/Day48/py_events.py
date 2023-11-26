from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = 'https://www.python.org/'
chrome_driver_path = 'C:\Developement\chromedriver.exe'

options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(URL)
menu = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul')
items = menu.find_elements(By.TAG_NAME, 'li')

events = dict()
for index, item in enumerate(items):
    date = item.find_element(By.TAG_NAME, 'time').text
    name = item.find_element(By.TAG_NAME, 'a').text
    events[index] = {
        'time': date ,
        'name': name
    }

print(events)
