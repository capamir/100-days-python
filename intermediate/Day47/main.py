from bs4 import BeautifulSoup
import requests

URL = 'https://www.amazon.com/ASUS-Gaming-Laptop-Nebula-Display/dp/B0BZQPQD63/ref=sr_1_1?crid=Y5P8ZE1RY9PC&th=1'
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept-Language': 'en-US,en;q=0.5'
}

def send_email(title, msg, link):
    password = 'tlplnolethtrcjdg'
    email_from = 'amir583121@gmail.com'
    email_to = 'amirhn.workmail@gmail.com'
    protocol = "smtp.gmail.com"
    
    with smtplib.SMTP(protocol) as connection:
        connection.starttls()
        connection.login(email_from, password)
        connection.sendmail(
            from_addr=email_from,
            to_addrs=email_to,
            msg=f"Subject:{title}\n\n{msg}\n{url}".encode("utf-8")
        )


response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')

price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_without_currency = ''.join(price_without_currency.split(','))
price_as_float = float(price_without_currency)

BUY_PRICE = 1800.00
if price_as_float <= BUY_PRICE:
    title = soup.find(id="productTitle").get_text().strip()
    message = f"{title} is now {price}"
    send_email(title, message, URL)