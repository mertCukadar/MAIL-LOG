
#import necessary packages
from settings import EMAIL_HOST , DATABASE_CONF
import smtplib
import os
import sys
from datetime import datetime
from email.mime.text import MIMEText
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

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


class DATABASE:
    def connect_database():
        conn = psycopg2.connect(
        database = DATABASE_CONF.DATABASES['default']['NAME'],
        user = DATABASE_CONF.DATABASES['default']['USER'],
        password = DATABASE_CONF.DATABASES['default']['PASSWORD'],
        host = DATABASE_CONF.DATABASES['default']['HOST'],
        port = DATABASE_CONF.DATABASES['default']['PORT'],
    )

        cursor= conn.cursor(cursor_factory = RealDictCursor)

        try:
            cursor.execute("SELECT 1")
            conn.commit()
        except (psycopg2.OperationalError , psycopg2.InterfaceError):
            print("CONNECTION FAILED")

