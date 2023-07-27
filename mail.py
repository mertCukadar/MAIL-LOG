from enum import Enum
import smtplib
from email.mime.text import MIMEText

class Transport_Security_layer_certification(Enum):
    TSL = 1
    SSL = 2
    SMART_TSL = 3

class MailSend:
    def __init__(self, mode):
        self.mode = mode

    def sendmail(self, mail_to, mail_subject, mail_body, mail_from, mail_message):
        EMAIL = 'your_email@example.com'  # Replace with your email address
        PASSWORD = 'your_email_password'  # Replace with your email password

        with smtplib.SMTP('smtp.example.com', 587) as smtp:  # Replace with your SMTP server and port
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL, PASSWORD)

            msg = MIMEText(mail_message, 'plain', 'utf-8')
            msg['Subject'] = mail_subject
            msg['From'] = EMAIL
            msg['To'] = mail_to

            # Select the appropriate email body based on the mode
            if self.mode == Transport_Security_layer_certification.TSL:
                msg.set_payload("This is a TSL email.\n\n" + mail_body)
            elif self.mode == Transport_Security_layer_certification.SSL:
                msg.set_payload("This is an SSL email.\n\n" + mail_body)
            elif self.mode == Transport_Security_layer_certification.SMART_TSL:
                msg.set_payload("This is a SMART_TSL email.\n\n" + mail_body)

            smtp.sendmail(msg['From'], msg['To'], msg.as_string())