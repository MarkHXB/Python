import smtplib

MY_MAIL = "xxxxx@gmail.com"
MY_PASSWORD = "xxxx"

def sendmail():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_MAIL,MY_PASSWORD)
    connection.sendmail(from_addr=MY_MAIL,
                        to_addrs="xxxx@gmail.com",
                        msg="Subject:LOOK UP\n\nThe ISS is above you in the sky.")
    connection.close()
