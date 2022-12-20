from email.message import EmailMessage
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(messages):
    email_sender = "jandj808946@gmail.com"
    password = "mdryhbbgtnbperdt"
    subject = "Azure Synapse Status Log"
    emails=['anikdavis@gmail,com',"anikdavis18@gmail.com"]
    email_message = MIMEMultipart()
    email_message['Subject'] = subject
    email_message['From'] = email_sender
    #email_message['To'] = 'jandj808946@gmail.com'
    html = '''<h1>Azure Synapse Status Log<h1>
    <div>'''+ messages+'''<div>'''
    email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, password)
        for i in emails:
            smtp.sendmail(email_sender ,i, email_string)
