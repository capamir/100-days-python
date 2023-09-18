"https://api.openweathermap.org/data/2.5/weather?q=Rasht,IR&appid=86ab9d6bf32ce083f7a2635e45b9651a"
"https://api.openweathermap.org/data/2.5/forecast/hourly?q=Rasht,IR&appid=86ab9d6bf32ce083f7a2635e45b9651a"

import requests
import smtplib

proxy = {
    'http' : 'http://192.168.223.119:8080',
    'https' : 'http://192.168.223.119:8080'
}

def get_weather_status():
    my_lat = 37.276241
    my_lng = 49.594749
    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "86ab9d6bf32ce083f7a2635e45b9651a"

    weather_params = {
        "lat": my_lat,
        "lon": my_lng,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(
        url=OWM_Endpoint,
        params=weather_params,
        proxies=proxy
    )
    data = response.json()
    return response.status_code, data['weather'][0]

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
            msg=f"Subject:Weather condition\n\n{msg}"
        )

status, data = get_weather_status()

if int(data['id']) < 700:
    weather_status = data["main"]
    send_email(msg=f"{weather_status} bring an umbrella")
