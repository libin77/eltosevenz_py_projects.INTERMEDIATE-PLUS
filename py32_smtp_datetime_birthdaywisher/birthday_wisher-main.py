import datetime as dt
import pandas
import random
import smtplib


def get_letter():
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as let_file:
        letter = let_file.read().replace("[NAME]", birthday_person["b_name"])
    return letter


def send_mail():
    my_email = "eltosevenz.pyapp@gmail.com"
    secret_key = "kcfx kdne hzhz ndjb"  # newApp@2024
    to_mail = birthday_person["email"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=secret_key)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_mail,
                            msg=f"Subject:Happy Birthday!\n\n{get_letter()}")


current_date = dt.datetime.now()
today = (current_date.month, current_date.day)

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day, data_row.b_name): data_row for (index, data_row) in birthdays_df.iterrows()}
for person in birthdays_dict:
    today_with_name = today + (person[2],)
    if today_with_name in birthdays_dict:
        birthday_person = birthdays_dict[today_with_name]
        send_mail()



