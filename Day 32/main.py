##################### Normal Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random

MY_EMAIL = "defrim.haliti@outlook.com"
MY_PASSWORD = "OutlookPA5$"


time = dt.datetime.now()
today_tuple = (time.month, time.day)


data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,4)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_content = contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.office365.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday \n\n{new_content}")





