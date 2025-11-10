import os,logging

def configure_logging_and_files(SOURCE_DIR,BACKUP_DIR,LOG_DIR):
    try:
        os.makedirs(LOG_DIR,exist_ok=True)
        log_path=os.path.join(LOG_DIR,f"{os.path.basename(SOURCE_DIR)}.log")
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler(log_path) ,logging.StreamHandler()])
        if not os.path.exists(SOURCE_DIR):
            logging.error(f"Source directory {SOURCE_DIR} does not exist.")
            raise FileNotFoundError(f"Source directory {SOURCE_DIR} does not exist.")
        os.makedirs(BACKUP_DIR,exist_ok=True)
        logging.info("Starting backup process...")
        logging.info("All Files configured Successfully")
    except Exception as e:
        logging.error(f"Error in configuring files and logging: {e}")
        raise e