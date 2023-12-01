from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdF57BCawMa2fZADSzeVMVvKr9Z_4SPJl2h3Ey1o3c7ZI5gug/viewform?usp=sf_link'
ZILLOW_URL = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.85611565144186%2C%22south%22%3A37.694379800978%2C%22east%22%3A-122.29840365771484%2C%22west%22%3A-122.56825534228516%7D%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A586501%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

class ZillowRentHouse:
    def __init__(self):
        self.url = ZILLOW_URL
        response = requests.get(ZILLOW_URL, headers=header)
        zillow_web_page = response.text
        self.soup = BeautifulSoup(zillow_web_page, 'html.parser')
    
    def get_data(self):
        self.get_links()
        self.get_prices()
        self.get_addr()

    def get_links(self):
        house_links = self.soup.select('article a')
        self.links = [house_links[index]["href"] for index in range(0, len(house_links),2)]

    def get_prices(self):
        prices_tags = self.soup.select('article span')
        self.prices = []

        for price in prices_tags:
            if '$' in price.getText():
                self.prices.append(price.getText())

    def get_addr(self):
        address_tags = self.soup.select('article address')
        self.addresses = [address.getText() for address in address_tags]

class HouseForm:
    address_field = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    price_field = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    link_field = '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    button = '/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div'
    
    def __init__(self):
        self.url = FORM_URL
        chrome_driver_path = 'C:\Developement\chromedriver.exe'
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def post_info(self, house):
        self.driver.get(self.url)
        sleep(2)
        # getting Form's fields and submit button
        address = self.driver.find_element(By.XPATH, self.address_field)
        price = self.driver.find_element(By.XPATH, self.price_field)
        link = self.driver.find_element(By.XPATH, self.link_field)
        submit_button = self.driver.find_element(By.XPATH, self.button)
        # putting informations
        address.send_keys(house['address'])
        price.send_keys(house['price'])
        link.send_keys(house['link'])
        submit_button.click()

    def iter_data(self, addresses, prices, links):
        for index in range(len(addresses)):
            data = {
                'address': addresses[index],
                'price': prices[index],
                'link': links[index]
            }
            self.post_info(data)

zillow = ZillowRentHouse()
zillow.get_data()

form = HouseForm()
form.iter_data(zillow.addresses, zillow.prices, zillow.links)