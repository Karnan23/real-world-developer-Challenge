import os, time, logging
from dotenv import load_dotenv
from monitor import system_checker, report_maker
from utils import setup_logging, send_email

load_dotenv()

SCAN_INTERVAL = int(os.getenv("SCAN_INTERVAL", 5))
TOTAL_CYCLES = int(os.getenv("TOTAL_CYCLES", 10))
LOG_DIR = os.getenv("LOG_DIR", "Logs")
LOG_FILE = os.getenv("OUTPUT_LOG_FILE", "system.log")
REPORT_DIR = os.getenv("REPORT_DIR", "Reports")
REPORT_FILE = os.getenv("REPORT_NAME", "report.json")

CPU_THRESHOLD = int(os.getenv("CPU_THRESHOLD", 80))
MEMORY_THRESHOLD = int(os.getenv("MEMORY_THRESHOLD", 85))
DISK_THRESHOLD = int(os.getenv("DISK_THRESHOLD", 90))

SMTP_SERVER = os.getenv("EMAIL_HOST")
SMTP_PORT = int(os.getenv("EMAIL_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("APP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_MAIL")


report_path = os.path.join(REPORT_DIR, REPORT_FILE)
log_path = setup_logging(LOG_DIR, LOG_FILE)

logging.info("Starting System Health Monitor...")


for cycle in range(TOTAL_CYCLES):
    logging.info(f"Starting system check cycle {cycle + 1} of {TOTAL_CYCLES}")
    details = system_checker(SCAN_INTERVAL, CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD)
    if details:
        report_maker(details, report_path)
    send_email(log_path, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL)
    time.sleep(SCAN_INTERVAL)

logging.info("System Health Monitoring completed.")
