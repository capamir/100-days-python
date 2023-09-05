import requests
from datetime import datetime

proxy = {
    'http' : 'http://192.168.98.126:8080',
    'https' : 'http://192.168.98.126:8080'
}
my_lat = 37.276241
my_lng = 49.594749

def get_iss_pos():
    URL = 'http://api.open-notify.org/iss-now.json'

    response = requests.get(
        url=URL, 
        proxies=proxy
    )
    response.raise_for_status()
    data = response.json()

    lng = data['iss_position']['longitude']
    lat = data['iss_position']['latitude']
    possition = {'lng': lng, 'lat': lat}
    return possition

def is_iss_overhead():
    pos = get_iss_pos()
    if my_lat-5 <= pos['lat'] <= my_lat+5 and my_lng-5 <= pos['lng'] <= my_lng+5:
        return True
    return False

def is_night(lat=37.276241, lng=49.594749):
    URl = 'https://api.sunrise-sunset.org/json'
    parameters ={
        'lat': float(lat),
        'lng': float(lng),
        'formatted': 0
    }
    response = requests.get(URl, params=parameters, proxies=proxy)
    response.raise_for_status()
    data = response.json()

    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    print(sunrise)
    print(sunset)
    print(time_now)
    return False

def send_email():
    password = 'tlplnolethtrcjdg'
    email_from = 'amir583121@gmail.com'
    email_to = 'amirhn.workmail@gmail.com'
    protocol = "smtp.gmail.com"
    with smtplib.SMTP(self.protocol) as connection:
            connection.starttls()
            connection.login(self.email_from, self.password)
            connection.sendmail(
                from_addr=self.email_from,
                to_addrs=self.email_to,
                msg=f"Subject:Look up👆\n\nISS satelite is right above you."
            )

if is_iss_overhead() and is_night():
    send_email()

