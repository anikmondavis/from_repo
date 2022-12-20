EMAIL_ADDRESS='anikdavis18@gmail.com'
EMAIL_PASSWORD='dlsaanik18'
'''
with smtplib.SMTP('smtp.gmail.com',587) as eml:
    eml.ehlo()
    eml.starttls()
    eml.smtp.ehlo()

    eml.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject='test image'
    body='how about test'
    msg=f'Subject:{subject}\n\nBody:{body}'
    eml.sendmail(EMAIL_ADDRESS,'anikdavis1999@gmail.com',msg)

import smtplib,ssl
context = ssl.create_default_context()

conn = smtplib.SMTP_SSL('imap.gmail.com',587,context)
conn.ehlo()
conn.starttls()
conn.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

conn.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,'Subject: What you like? \n\n Reply Reply Reply')
conn.quit()
'''

# import smtplib
# from email.utils import formataddr
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# msg = MIMEMultipart()
# body_part = MIMEText('Write you text here.')
# user = EMAIL_ADDRESS
# password = EMAIL_PASSWORD
# msg['Subject'] = 'anik'
# msg['From'] = user
# msg['To'] = 'anikdavis18@gmail.com'
# msg.attach(body_part)
# smtp_obj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# smtp_obj.login(user, password)
# smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
# smtp_obj.quit()
import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def mail(messages):
    email_sender = "anikdavis18@gmail.com"
    password = "mbgsypukvwzuduot"
    subject = "Azure Synapse Status Log"
    emails=['anikdavis18@gmail.com','anikdavis@gmail.com']
    email_message = MIMEMultipart()
    email_message['Subject'] = subject
    email_message['From'] = email_sender
    dir_path = "C:/Users/anikmon.davis/Documents/img"
    entries = os.listdir('C:/Users/anikmon.davis/Documents/img')
    for f in entries:  # add files to the message
        file_path = os.path.join(dir_path, f)
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename=f)
        email_message.attach(attachment)
    
   # html = '''<h3>Azure Synapse Status Log</h3>
    #<div>'''+ messages+'''<div>'''

    
    #email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, password)
        for i in emails:
            smtp.sendmail(email_sender, i, email_string)

mail('hello')
print("Email has been sent to anikdavis18@gmail.com")
