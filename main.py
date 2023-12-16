import smtplib
from dotenv import load_dotenv
import os

load_dotenv()




my_email = "hassan.elwany1987@gmail.com"
my_password = os.getenv("PASSWORD")

connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="elwany_hassan@hotmail.com", msg="Hello")
connection.close()