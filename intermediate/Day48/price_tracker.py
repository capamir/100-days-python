from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = 'https://www.amazon.com/ASUS-Gaming-Laptop-Nebula-Display/dp/B0BZQPQD63/ref=sr_1_1?crid=Y5P8ZE1RY9PC&th=1'
chrome_driver_path = 'C:\Developement\chromedriver.exe'

options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(URL)
price  = driver.find_element(By.CLASS_NAME, 'a-price')
print(price.text)
