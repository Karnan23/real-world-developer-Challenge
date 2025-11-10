# 🧠 Day 9 – Automated Backup & Versioning System
<br/>

---

## 🔍 Overview

The **Automated Backup & Versioning System** is a real-world Python automation project designed to perform **scheduled folder backups with version control**.  
It automatically compresses the selected directory into timestamped ZIP files and removes older backups once the version limit is reached — mimicking enterprise-grade backup retention systems.

---

## ⚙️ Key Features

- ✅ Automatically creates versioned ZIP backups  
- ✅ Retains only the latest N backups (configurable via `.env`)  
- ✅ Logs every operation (created, deleted, skipped)  
- ✅ Modular architecture — easily reusable and extendable  
- ✅ Works on all OS (Windows / Linux / macOS)  
- ✅ Real-world DevOps-style logging and error handling  

---

## 🧩 Tech Stack

| **Component**      | **Technology**                     |
| ------------------ | ---------------------------------- |
| **Language**       | Python 3.x                         |
| **Libraries**      | `os`, `zipfile`, `logging`, `datetime`, `python-dotenv` |
| **Configuration**  | `.env` file                        |
| **Logging**        | Dual output — console + log file   |
| **Output**         | Versioned `.zip` backups in `Backups/` directory |

---

## 🗂️ Project Structure
```bash
Day_9_Automated_Backup_Versioning_System/
│
├── main.py                # Entry point - orchestrates config and backup
├── backup.py              # Handles compression and version cleanup
├── utils.py               # Logging setup and validation
├── .env                   # Environment configuration (not tracked in Git)
├── .gitignore             # Ignored files & sensitive data
├── requirements.txt       # Dependencies
├── Logs/
│   └── project_data.log   # Auto-generated log file
└── Backups/
    └── backup_2025-11-09_11-38-06.zip   # Example backup file
```
---

## ⚙️ .env Configuration Example
```bash
# ===== Backup Configuration =====
SOURCE_DIR=./Project_data
BACKUP_DIR=./Backups
LOG_DIR=./Logs
RETENTION_LIMIT=5
BACKUP_PREFIX=backup
```
---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Karnan23/Day_9_Automated_Backup_Versioning_System.git
cd Day_9_Automated_Backup_Versioning_System
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Configure Environment

Edit the .env file according to your folder paths and limits.

### 4️⃣ Run the Backup System
```bash
python main.py
```
---

## 📊 Sample Console Output
```bash
2025-11-09 11:38:00 - INFO - Starting backup process...
2025-11-09 11:38:06 - INFO - Created backup: backup_2025-11-09_11-38-06.zip
2025-11-09 11:38:06 - INFO - Total backups in the Backups folder : 6
2025-11-09 11:38:06 - INFO - Deleted oldest backup : backup_2025-11-02_09-14-00.zip
2025-11-09 11:38:06 - INFO - Backup process completed successfully.
```
---

## ⚙️ Real-World Use Cases

1. Automated project folder snapshots

2. Daily or hourly DevOps configuration backups

3. Versioned archives for local data management

4. Lightweight alternative to enterprise backup tools

---

## 🧰 Requirements
```bash
python-dotenv==1.2.1
```
---

## 🧠 Learning Outcomes

By completing this project, you’ve mastered:

- Real-world file compression & automation logic

- Backup version management with retention policy

- Config-driven Python scripting

- Logging, validation, and structured project design

- Scalable modular coding — ready for DevOps or AI pipeline use

---

## 🧑‍💻 Author

Karnan G

**💬 “Don’t write code for practice. Write code that could run in production.”**

---