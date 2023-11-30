from bs4 import BeautifulSoup
import requests

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdF57BCawMa2fZADSzeVMVvKr9Z_4SPJl2h3Ey1o3c7ZI5gug/viewform?usp=sf_link'
ZILLOW_URL = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.85611565144186%2C%22south%22%3A37.694379800978%2C%22east%22%3A-122.29840365771484%2C%22west%22%3A-122.56825534228516%7D%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A586501%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(ZILLOW_URL, headers=header)
zillow_web_page = response.text

soup = BeautifulSoup(zillow_web_page, 'html.parser')

house_links = soup.select('article a')
links = [house_links[index]["href"] for index in range(0, len(house_links),2)]

prices_tags = soup.select('article span')
prices = []

for price in prices_tags:
    if '$' in price.getText():
        prices.append(price.getText())

address_tags = soup.select('article address')
addresses = [address.getText() for address in address_tags]

