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
