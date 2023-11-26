
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = 'http://secure-retreat-92358.herokuapp.com/'
chrome_driver_path = 'C:\Developement\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)

options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)

# input elements
first_name  = driver.find_element(By.NAME, 'fName')
last_name= driver.find_element(By.NAME, 'lName')
email= driver.find_element(By.NAME, 'email')

# values
first_name.send_keys('Amirhossein')
last_name.send_keys('Noruzi')
email.send_keys('amir583121@gmail.com')

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

while True:
    pass
