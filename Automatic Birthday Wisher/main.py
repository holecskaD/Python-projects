##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt

today = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")

MY_EMAIL = "davidholecska@gmail.com"
MY_PASSWORD = " ljashdfjlkasjhnf"

for index, row in birthdays.iterrows():
    letter_str = ""
    if row["year"] == today.year and row["month"] == today.month and row["day"] == today.day:
        today_bd_name = row["name"]
        today_bd_email = row["email"]
        letter_number = random.randint(1, 3)
        first_line = f"Dear {today_bd_name}, \n "

        if letter_number == 1:
            with open("letter_templates/letter_1.txt", "r") as letter:
                lines = letter.readlines()
                lines[0] = first_line
        elif letter_number == 2:
            with open("letter_templates/letter_2.txt", "r") as letter:
                lines = letter.readlines()
                lines[0] = first_line
        else:
            with open("letter_templates/letter_3.txt", "r") as letter:
                lines = letter.readlines()
                lines[0] = first_line

        for lines in lines:
            letter_str += lines

        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls() #titkosítás
        #     connection.login(MY_EMAIL, MY_PASSWORD)
        #     connection.sendmail(
        #         from_addr=MY_EMAIL,
        #         to_addrs=today_bd_email,
        #         msg=f"Subject: Happy Birthday! \n\n {letter_str} ")
