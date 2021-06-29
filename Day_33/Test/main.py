import smtplib

MY_MAIL = "testingerG22@gmail.com"
MY_PASSWORD = "centhon7#"

def sendmail():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_MAIL,MY_PASSWORD)
    connection.sendmail(from_addr=MY_MAIL,
                        to_addrs="bakonyimark8@gmail.com",
                        msg="Subject:LOOK UP\n\nThe ISS is above you in the sky.")
    connection.close()
