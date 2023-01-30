##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = "frostpie4@gmail.com" # Ypur Email
MY_PASSWORD = "jdbvlvnvrskfnobj" # Your password

# current date-time using now() function in datetime class within datetime module
today = dt.datetime.now()
# created a tuple which stores current month and current day
today_tuple = (today.month, today.day)

# read data from csv which holds the birthday data of your friends and family
birthday_data = pandas.read_csv("birthdays.csv")

# created a dictionary using dictionary-comprehension which has the key in the form of tuple=(month, day) and value as the entire data of an individual person like their name, birth date, month, year and email
birthday_dict = {(row.month, row.day) : row for (index, row) in birthday_data.iterrows()}

# This block of code runs if the data in 'today_tuple' is same as any of the key in 'birthday_data' dictionary
if today_tuple in birthday_dict:
    # 'birthday_person' variable hold the data of the person whose birth-date is matched with today's date
    birthday_person = birthday_dict[today_tuple]

    # selects a random birthday letter template from the 'letter_templates' folder
    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        letter_content = letter.read()
        # replace the placeholder with the actual name of the birthday person using replace() function
        letter_content = letter_content.replace("[NAME]", birthday_person["name"])

    # make a connection with the mail server using SMTP() class in smtplib library and set the sever as per your email like 'smtp.gmail.com' for Gmail
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # encrypt the connection using starttls() function
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter_content}"
        )