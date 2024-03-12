import datetime as dt
import random
import smtplib

my_email = "eltosevenz.pyapp@gmail.com"
secret_key = "kcfx kdne hzhz ndjb"  # newApp@2024
to_mail = "sumilibinl77@gmail.com"


def get_quotes():
    quotes = "nothing"
    with open("quotes.txt") as quotes_file:
        quotes = random.choice(quotes_file.readlines())
    return quotes


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=secret_key)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_mail,
                            msg=f"Subject:Quotes of the Day\n\n{get_quotes()}")


current_date = dt.datetime.now()
if current_date.weekday() == 1:
    send_mail()




