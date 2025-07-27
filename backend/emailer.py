import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()  # ✅ Load .env variables

from_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

def send_email(product_name, url, price, to_email):
    msg = EmailMessage()
    msg["Subject"] = f"🔥 Price Drop Alert: {product_name}"
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(
        f"The product '{product_name}' is now ₹{price}!\nCheck it out here: {url}"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.send_message(msg)
