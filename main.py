import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import random
import pandas as pd
import os

load_dotenv()


now = dt.datetime.now()
data = pd.read_csv("./birthdays.csv")
my_email = "hassanwebdevt@gmail.com"
my_password = os.getenv("PASSWORD")
data_list = data.to_dict('records')


for row in data_list:
    email = row['email']
    year = int(row['year'])
    month = int(row['month'])
    day = int(row['day'])
    name = row['name']

    if now.month == month and now.day == day:
        random_message = random.choice(os.listdir("./letter_templates"))
        with open(f"./letter_templates/{random_message}", "r") as file:
            message = file.readlines()
            modified_line = message[0].replace('[NAME]', name)
            modified_message = modified_line + ''.join(message[1:])

        with open("quotes.txt", "r") as file:
            quotes_lines = file.readlines()
            quote = random.choice(quotes_lines).split("-")

            with smtplib.SMTP("smtp.gmail.com") as connection:

                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=f"{email}",
                    msg=f"Subject:BirthDay!\n\n {modified_message}"

                )
