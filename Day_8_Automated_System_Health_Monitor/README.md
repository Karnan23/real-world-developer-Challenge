# 🧠 Day 8 – Automated System Health Monitor
<br/>

## 🔍 Overview

The **System Health Monitor** is a real-world automation tool built using pure Python.
It continuously monitors **CPU, Memory, and Disk usage**, logs performance data, and automatically sends **email alerts** when system thresholds are breached.

This project mimics a lightweight internal monitoring agent — similar to what IT and DevOps teams use for server health tracking and automated performance alerting.

---

## ⚙️ Key Features

- ✅ Real-time system health tracking using psutil
- ✅ Logs CPU, RAM, and Disk usage in both console and file
- ✅ Configurable thresholds via .env file
- ✅ Email alerts for abnormal system usage
- ✅ Appends each check to a persistent report file
- ✅ Modular architecture (main.py, monitor.py, utils.py)
- ✅ Works cross-platform (Windows / Linux / macOS)

---

## 🧩 Tech Stack

| **Component**      | **Technology**                                                |
| ------------------ | ------------------------------------------------------------- |
| **Language**       | Python 3.x                                                    |
| **Libraries**      | `psutil`, `python-dotenv`, `smtplib`, `logging`, `email.mime` |
| **Configuration**  | `.env` file                                                   |
| **Logging**        | Rotating file + console handler                               |
| **Alert Delivery** | SMTP Email (TLS-secured)                                      |

---

## 🗂️ Project Structure
```bash
Day_8_System_Health_Monitor/
│
├── main.py                # Entry point - orchestrates all modules
├── monitor.py             # System checks & report generation
├── utils.py               # Logging setup & email handling
├── .env                   # Environment variables (not tracked in Git)
├── .gitignore             # Ignored files & sensitive data
├── requirements.txt       # Python dependencies
├── Logs/
│   └── system.log         # Auto-generated logs
└── Reports/
    └── report.json        # Auto-generated report data
```
---

## ⚙️ .env Configuration Example
```bash
# ====== System Config ======
SCAN_INTERVAL=5
TOTAL_CYCLES=10

# ====== Thresholds ======
CPU_THRESHOLD=75
MEMORY_THRESHOLD=80
DISK_THRESHOLD=85

# ====== Paths ======
LOG_DIR=Logs
OUTPUT_LOG_FILE=system.log
REPORT_DIR=Reports
REPORT_NAME=report.json

# ====== Email Config ======
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECEIVER_MAIL=receiver_email@gmail.com
```
---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Day_8_System_Health_Monitor.git
cd Day_8_System_Health_Monitor
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Configure Environment

Create a .env file in the project root using the example above.

### 4️⃣ Run the Monitor
```bash
python main.py
```
---

## 📊 Sample Console Output
```bash
2025-11-06 12:15:21 - INFO - Starting System Health Monitor...
2025-11-06 12:15:26 - INFO - CPU: 23% | Memory: 68% | Disk: 57%
2025-11-06 12:15:26 - INFO - System is working well and good
2025-11-06 12:15:26 - INFO - Report generated successfully.
2025-11-06 12:15:26 - INFO - No alerts found in the latest cycle. Email not sent.
```

## ⚠️ Example Alert Trigger
```bash
2025-11-06 12:35:54 - WARNING - Alert: High CPU usage detected: 92%
2025-11-06 12:35:54 - INFO - Alert email sent successfully for current cycle.
```
---

## 💡 Real-World Use Cases

- Local system performance tracking

- Automated alerting for high CPU/memory usage

- Cron job integration for server uptime monitoring

- Extendable into a dashboard or AI-driven monitoring service

---

## 🧰 Requirements
```bash
psutil==7.1.2
python-dotenv==1.2.1
```
---

## 🧠 Learning Outcomes

By completing this project, you’ve mastered:

- Modular project structuring

- Logging and error handling best practices

- Config-driven automation via .env

- Email integration with Python’s smtplib

- Real-world DevOps monitoring patterns

---

## 🧑‍💻 Author

Karnan G

**💬 “Don’t write code for practice. Write code that could run in production.”**

---
