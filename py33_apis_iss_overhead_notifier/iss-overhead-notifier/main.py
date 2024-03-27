import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 8.576191  # Your latitude
MY_LONG = 76.901021  # Your longitude
RADIUS = 5
my_email = "eltosevenz.pyapp@gmail.com"
secret_key = "kcfx kdne hzhz ndjb"  # newApp@2024
to_mail = "sumilibinl77@gmail.com"


def is_iss_overhead():
    iss_now_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_now_response.raise_for_status()
    iss_data = iss_now_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT + RADIUS >= iss_latitude >= MY_LAT - RADIUS
            and MY_LONG + RADIUS >= iss_longitude >= MY_LONG - RADIUS):
        return True

    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if not sunrise > time_now < sunset:
        return True

    return False


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=secret_key)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_mail,
                            msg="Subject:ISS Overhead Notification\n\nISS is above you in your sky")

while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        send_mail()
