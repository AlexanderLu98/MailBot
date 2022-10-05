import smtplib
import ssl

def sendEmail(msg):
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "alexanderbottester@gmail.com"
    password = "alexan2710"
    receiver_email = "alex.lu2710@gmail.com"

    context = ssl.create_default_context()

    connection = smtplib.SMTP_SSL(smtp_server, port, context=context)
    connection.login(sender_email,password)
    connection.sendmail(sender_email, receiver_email, msg)

sendEmail("test")