import os, logging, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def setup_logging(log_dir, log_file):
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_path), logging.StreamHandler()]
    )
    return log_path


def send_email(log_path, smtp_server, smtp_port, sender_email, sender_pass, receiver_email):
    try:
        with open(log_path, "r") as file:
            lines = file.readlines()

        cycle_lines = []
        for line in reversed(lines):
            cycle_lines.append(line)
            if "cycle" in line.lower():
                break
        cycle_lines = cycle_lines[::-1]
        alerts = [line for line in cycle_lines if "alert" in line.lower()]

        if not alerts:
            logging.info("No alerts found in latest cycle. Email not sent.")
            return

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "🚨 System Health Alert"
        msg.attach(MIMEText("".join(alerts), "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_pass)
            server.send_message(msg)

        logging.info("Alert email sent successfully for current cycle.")
    except Exception as e:
        logging.exception("Failed to send alert email.")
