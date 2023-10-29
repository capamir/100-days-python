import requests
import smtplib


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_apikey = "DJGSPDYHJMV2PF0X"
news_apikey = "8038ea308b054859a24868d07024c0f0"

def send_email(msg):
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
            msg=f"Subject:Tesla Stock News\n\n{msg}"
        )

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_apikey
}
res = requests.get(STOCK_ENDPOINT, params=stock_params)
data = res.json()['Time Series (Daily)']
data_list = [value for value in data.values()][:2]

yesterday_close = data_list[0]["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_close = data_list[1]["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff_price = abs(float(yesterday_close) - float(day_before_yesterday_close))

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = (diff_price / float(yesterday_close)) * 100

# If TODO4 percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if diff_percentage < 1:
    news_params = {
        "apiKey": news_apikey,
        "qInTitle": COMPANY_NAME,
    }
    res = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = res.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]


    # Create a new list of the first 3 article's headline and description using list comprehension.
    messages = [f"Headline: {article['title']}\n brief: {article['description']}" for article in three_articles]
    # Send each article as a separate message via Twilio. 
    for message in messages:
        send_email(message.encode('utf-8'))
    print('email sent')


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

