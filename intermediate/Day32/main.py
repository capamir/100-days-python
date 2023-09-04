import smtplib
from datetime import datetime
from random import choice


class Mail:
    password = 'tlplnolethtrcjdg'
    email_from = 'amir583121@gmail.com'
    email_to = 'amirhn.workmail@gmail.com'
    protocol = "smtp.gmail.com"

    def __init__(self):
        if self.is_monday():
            self.send_mail()

    @staticmethod
    def is_monday():
        now = datetime.now()
        weekday = now.weekday()
        return weekday == 0

    @staticmethod
    def get_motivation():
        with open('./quotes.txt') as f:
            all_quotes = f.readlines()
            quote = choice(all_quotes)
            print(quote)
            return quote

    def send_mail(self):
        with smtplib.SMTP(self.protocol) as connection:
            connection.starttls()
            connection.login(self.email_from, self.password)
            connection.sendmail(
                from_addr=self.email_from,
                to_addrs=self.email_to,
                msg=f"Subject:Monday motivation\n\n{self.get_motivation()}"
            )

Mail()