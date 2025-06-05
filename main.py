import subprocess
import smtplib
from email.mime.text import MIMEText

# When disk usage >= 80%, send alert
THRESHOLD = 80

# Email setup
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_MAIL = "abidshovon945@gmail.com"
SENDER_PASSWORD = "---- ---- ---- ----"    # Use 16 digit gmail app password. Ex: "zskc yvlo uevj tafm"
RECEIVED_MAIL = "shovonhasan333@gmail.com"

def check_disk_usage():
    result = subprocess.run(["df", "-h"], stdout=subprocess.PIPE, text=True)
    store_lines = result.stdout.strip().split('\n')[1:]
    alert_list = []

    for store_line in store_lines:
        parts = store_line.split()
        if len(parts) < 6:
            continue
        filesystem, size, used, avail, percent, mountpoint = parts
        percent_value = int(percent.replace('%', ''))
        if percent_value >= THRESHOLD:
            alert_list.append((filesystem, size, used, avail, percent, mountpoint))
            
    return alert_list


def send_email_alert(alerts):
    message_body = "Low Disk Space Alert:\n\n"
    
    for free_space in alerts:
        message_body += f"Mount Point: {free_space[5]}\n"
        message_body += f"Used: {free_space[2]} / Total: {free_space[1]} ({free_space[4]} used)\n\n"
    
    email_msg = MIMEText(message_body)
    email_msg["Subject"] = "Laptop Disk Space Alert"
    email_msg["From"] = SENDER_MAIL
    email_msg["To"] = RECEIVED_MAIL
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_MAIL, SENDER_PASSWORD)
            server.send_message(email_msg)
        print("Email alert sent successfully!")
    except Exception as e:
        print("Failed to send email.", e)


if __name__ == "__main__":
    notify = check_disk_usage()
    if notify:
        send_email_alert(notify)
    else:
        print("Enough disk space available.")
