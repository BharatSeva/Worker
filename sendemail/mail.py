import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .category import select_message
from dotenv import load_dotenv
import os
load_dotenv()

SMTP_HOST=os.getenv("SMTP_HOST")
SMTP_PORT=os.getenv("SMTP_PORT")
SMTP_EMAIL=os.getenv("SMTP_EMAIL")
SMTP_PASSWORD=os.getenv("SMTP_PASSWORD")

sender_email = SMTP_EMAIL 
sender_password = SMTP_PASSWORD 

def send_mail(data):
    mail = select_message(data)
    if not mail:
        print("Missed Testcase Detected", data)
        return

    user_email = data.get('hip_email') or data.get('email')
    # user_email = "tron21vaibhav@gmail.com"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = mail["subject"]
    message["From"] = sender_email
    message["To"] = user_email
    message.attach(MIMEText(mail["body"], "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")