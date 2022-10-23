from email.message import EmailMessage
from pass_1 import app_pass
import ssl
import smtplib

email_sender = "kirokoyoga@gmail.com"
email_password = app_pass

email_receiver = "kawip88065@ilusale.com "

subject = "Don't forget my email"
body = """
My email is coming right away
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string)
