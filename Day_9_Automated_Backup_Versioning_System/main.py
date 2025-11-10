import os, logging
from dotenv import load_dotenv
from utils import configure_logging_and_files
from backup import create_backup

load_dotenv()

# Configure logging
LOG_DIR = os.getenv("LOG_DIR", "logs.log")
SOURCE_DIR = os.getenv("SOURCE_DIR", "Project_data")
BACKUP_DIR = os.getenv("BACKUP_DIR", "backups")
VERSION_LIMIT = int(os.getenv("RETENTION_LIMIT", 5))
BACKUP_NAME=os.getenv("BACKUP_PREFIX","backup")

configure_logging_and_files(SOURCE_DIR,BACKUP_DIR,LOG_DIR)

if __name__ == "__main__":
    try:
        create_backup(BACKUP_NAME,SOURCE_DIR,BACKUP_DIR,VERSION_LIMIT)
        logging.info("Backup process completed successfully.")
    except Exception as e:
        logging.error(f"Backup process failed: {e}")


