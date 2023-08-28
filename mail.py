from enum import Enum
import smtplib
from email.mime.text import MIMEText
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from  settings import EMAIL_HOST 


class MailSend:
    @staticmethod
    def sendmail(mail_to, mail_subject, mail_body, mail_message, data_list, html_file_path):
        try:
            smtp = smtplib.SMTP(EMAIL_HOST['EMAIL_HOST'], EMAIL_HOST['EMAIL_PORT'])
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_HOST['EMAIL_HOST_USER'], EMAIL_HOST['EMAIL_HOST_PASSWORD'])

            msg = MIMEMultipart()
            msg['Subject'] = mail_subject
            msg['From'] = EMAIL_HOST['EMAIL_HOST_USER']
            msg['To'] = mail_to

            # Verileri HTML tablosuna dönüştür
            if len(data_list) > 0:
                data_table = '<table style="border-collapse: collapse; width: 100%;">'
                data_table += '<tr>'
                for key in data_list[0].keys():
                    if key == 'alarm_class':
                        key = "alarm destination"
                        data_table += f'<th style="border: 1px solid black; padding: 8px; text-align: left;">{key}</th>'
                    else:
                        data_table += f'<th style="border: 1px solid black; padding: 8px; text-align: left;">{key}</th>'
                data_table += '</tr>'
                for data in data_list:
                    data_table += '<tr>'
                    for value in data.values():
                        if value == False:
                            data_table += f'<td style="border: 1px solid black; padding: 8px; text-align: left;">True</td>'
                        else:    
                            data_table += f'<td style="border: 1px solid black; padding: 8px; text-align: left;">{value}</td>'
                        if value == "":
                            value = datetime.datetime.now()
                            value = value.strftime("%Y-%m-%d %H:%M:%S")
                            data_table += f'<td style="border: 1px solid black; padding: 8px; text-align: left;">{value}</td>'
                    data_table += '</tr>'
                data_table += '</table>'
            else:
                data_table = ''
            # HTML dosyasını içe aktar
            with open(html_file_path, 'r') as html_file:
                html_content = html_file.read()

            # E-posta içeriğini oluştur
            email_content = f"""\
            {mail_message}
            {mail_body}
            {html_content}
            {data_table}
            """

            msg.attach(MIMEText(email_content, 'html'))

            smtp.sendmail(msg['From'], msg['To'], msg.as_string())
            print("E-posta başarıyla gönderildi.")
        except Exception as e:
            print("E-posta gönderilirken bir hata oluştu:", str(e))
        finally:
            return True
        

