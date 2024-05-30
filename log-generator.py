import logging
import time
import requests
import json

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)

# URL для надсилання логів до Fluentd
FLUENTD_HTTP_ENDPOINT = 'http://localhost:8080'

# Функція для надсилання логів до Fluentd
def send_log(level, message):
    log_entry = {
        'level': level,
        'message': message,
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(FLUENTD_HTTP_ENDPOINT, headers=headers, data=json.dumps(log_entry))
        if response.status_code != 200:
            logging.error(f"Failed to send log to Fluentd: {response.text}")
    except Exception as e:
        logging.error(f"Error sending log to Fluentd: {e}")

# Проста функція для генерації логів
def generate_logs():
    while True:
        send_log("INFO", "This is an info log")
        send_log("WARNING", "This is a warning log")
        send_log("ERROR", "This is an error log")
        time.sleep(5)  # Генерація логів кожні 5 секунд

if __name__ == "__main__":
    generate_logs()
