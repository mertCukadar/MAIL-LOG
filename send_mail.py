
#import necessary packages
from settings import EMAIL_HOST
import smtplib
import os
import sys
from datetime import datetime
from email.mime.text import MIMEText

class MailSend:
    def sendmail(self, mail_to, mail_subject, mail_body , mial_from , mail_massage):
        EMAIL = EMAIL_HOST.EMAIL_HOST_USER
        PASSWORD = EMAIL_HOST.EMAIL_HOST_PASSWORD

        with smtplib.SMTP(EMAIL, 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL, PASSWORD)

            msg = MIMEText(mail_massage , 'plain' , 'utf-8')
            msg['Subject'] = mail_subject
            msg['From'] = EMAIL
            msg['To'] =  mail_to
            
            smtp.sendmail(msg['From'], msg['To'], msg.as_string()) 
