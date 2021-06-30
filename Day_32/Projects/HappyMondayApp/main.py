import random
import datetime as dt
import smtplib

#fourth
MY_MAIL = "xxxx@gmail.com"
MY_PASSWORD = "xxxx"
SMTP_PROVIDE = "smtp.gmail.com"

#first
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    # second
    with open("../quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)
        connection = smtplib.SMTP(SMTP_PROVIDE)
        connection.starttls()
        connection.login(user=MY_MAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs="xxxx@yahoo.com",
                            msg=f"Subject:Happy Monday!\n\n{quote}")
        connection.close()
        print("The mail sent successfully")
else:
    print("Perhaps today is not monday")


