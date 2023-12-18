import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import random
import pandas as pd

load_dotenv()


def generate_modified_message(name, template_path):
    """
    Generate a modified message by replacing a placeholder with the given name.

    Parameters:
    - name (str): The name to be inserted into the message.
    - template_path (str): The path to the template file.

    Returns:
    - str: The modified message.
    """
    with open(f"{template_path}", "r") as file:
        message = file.readlines()
        modified_line = message[0].replace('[NAME]', name)
        return modified_line + ''.join(message[1:])


def send_birthday_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Send a birthday email using Gmail SMTP.

    Parameters:
    - sender_email (str): Sender's email address.
    - sender_password (str): Sender's email password.
    - recipient_email (str): Recipient's email address.
    - subject (str): Email subject.
    - body (str): Email body.
    """
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Subject:{subject}\n\n {body}"
        )


def main():
    """
    Main function to automate birthday wishes.

    Reads birthday data, checks for today's birthdays, generates modified messages,
    and sends birthday emails.
    """
    now = dt.datetime.now()
    data = pd.read_csv("./birthdays.csv")
    my_email = "hassanwebdevt@gmail.com"
    my_password = os.getenv("PASSWORD")

    template = random_message = random.choice(os.listdir('./letter_templates'))
    template_path = f'./letter_templates/{template}'

    data_list = data.to_dict('records')

    for row in data_list:
        email = row['email']
        year = int(row['year'])
        month = int(row['month'])
        day = int(row['day'])
        name = row['name']

        if now.month == month and now.day == day:
            # print("yes")
            modified_message = generate_modified_message(
                name=name, template_path=template_path)

            send_birthday_email(sender_email=my_email, sender_password=my_password,
                                recipient_email=email, subject="BirthDay!", body=modified_message)


if __name__ == "__main__":
    main()
