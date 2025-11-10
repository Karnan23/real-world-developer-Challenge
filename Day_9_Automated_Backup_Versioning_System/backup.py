import os, datetime, logging
from zipfile import ZipFile

def create_backup(BACKUP_NAME, SOURCE_DIR, BACKUP_DIR,VERSION_LIMIT):
    try:
        backup_name = f"{BACKUP_NAME}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.zip"
        backup_folder = os.path.join(BACKUP_DIR, backup_name)
        with ZipFile(backup_folder, "w") as zip:
            for root, dirs, files in os.walk(SOURCE_DIR):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip.write(file_path, os.path.relpath(file_path, SOURCE_DIR))
                    logging.info(f"{file} is added to Zip archive successfully ")
            logging.info("All project files are archive successfully")
        logging.info(f"Created backup: {backup_name}")
        logging.info("Backup creation completed")
        manage_backup_versions(BACKUP_DIR, VERSION_LIMIT)
    except Exception as e:
        logging.error(f"Error during backup creation: {e}")


def manage_backup_versions(BACKUP_DIR, VERSION_LIMIT):
    logging.info("Managing backup versions")
    try:
        for root, _, files in os.walk(BACKUP_DIR):
                    logging.info(f"Total backups in the Backups folder : {len(files)}")
                    if len(files) > VERSION_LIMIT:
                        for _ in range(VERSION_LIMIT,len(files)):
                            os.remove(os.path.join(root, files[0]))
                            logging.info(f"Deleted oldest backup : {files[0]} ")
                            files.pop(0)
                    else:
                        logging.info("No old backups to delete")
        logging.info("Backup version management completed")
    except Exception as e:
         logging.error(f"Error during backup version management: {e}")