import requests
import json
from datetime import date
import time
import smtplib, ssl

port = 465  # For SSL
#provide sender gmail account password 
password = "####"

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

#sender email address
sender_email = "XXX@gmail.com"
#receiver email address
receiver_email = "YYY@gmail.com"
message = "Vaccine slot is available in itarsi, Please book it"
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
