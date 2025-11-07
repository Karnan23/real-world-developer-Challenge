import psutil, datetime, logging, os

def system_checker(SCAN_INTERVAL, CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD):
    try:
        cpu = psutil.cpu_percent(SCAN_INTERVAL)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        logging.info(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

        alerts = []
        if cpu > CPU_THRESHOLD:
            alerts.append(f"High CPU usage detected: {cpu}%")
        if memory > MEMORY_THRESHOLD:
            alerts.append(f"High Memory usage detected: {memory}%")
        if disk > DISK_THRESHOLD:
            alerts.append(f"High Disk usage detected: {disk}%")

        if alerts:
            for a in alerts:
                logging.warning(f"Alert: {a}")
        else:
            logging.info("System is working well and good")

        result = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cpu": cpu,
            "memory": memory,
            "disk": disk,
            "alerts": alerts
        }
        return result
    except Exception as e:
        logging.exception("System check failed")
        return None


def report_maker(system_details, report_path):
    try:
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        with open(report_path, "a") as file:
            file.write(f"{system_details}\n")
        logging.info("Report generated successfully.")
    except Exception as e:
        logging.exception("Report generation failed")
