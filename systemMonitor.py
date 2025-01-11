import datetime

import psutil
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
file = "systemMonitor.json"
def send_alert(subject, body):
    sender_email = "sahan9976@gmail.com"
    receiver_email = "sahaniloy389@gmail.com"
    password = "Niiloy5335"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Alert sent successfully!")
    except Exception as e:
        print(f"Error sending alert: {e}")

def save_result(filepath, new_data):
    try:
        with open(filepath, "r") as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(new_data)

    with open(filepath, "w") as f:
        json.dump(existing_data, f, indent=4)


def monitor_system():
    data = {"timestamp": datetime.datetime.now().isoformat()}
    cpu_usage = psutil.cpu_percent(interval=1)
    data["cpu_usage"] = cpu_usage
    if cpu_usage>80:
        send_alert("High CPU Usage Alert", f"CPU usage is at {cpu_usage}%")

    disk = psutil.disk_usage('/')
    data["disk_percent"] = disk.percent
    if disk.percent > 90:
        send_alert("Low Disk Space Alert", f"Disk Usage is at {disk.percent}%")

    net = psutil.net_io_counters()
    data["net"] = net.bytes_sent
    if net.bytes_sent > 1e9:
        send_alert("High Network Usage Alert", f"Bytes sent: {net.bytes_sent / 1e6} MB")

    save_result(file, data)
    print("Monitoring Complete!")

if __name__ == "__main__":
    monitor_system()