import smtplib
from email.message import EmailMessage

def send_alert(ip, isp, time):
    msg = EmailMessage()
    msg.set_content(f"Alert! AP at {ip} (ISP: {isp}) went offline at {time}.")
    msg['Subject'] = 'ConnectX - AP Offline Alert'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient_email@example.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_password')
        smtp.send_message(msg)