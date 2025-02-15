import time
import requests
import logging
from datetime import datetime

logging.basicConfig(
    filename="uptime_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


URLS = [
    "http://www.example.com/nonexistentpage",
    "http://httpstat.us/404",
    "http://httpstat.us/500",
    "https://www.google.com/",
]


def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        status_message = f"Status Code: {status_code} {response.reason}"
        print(f"Checking URL: {url}")
        print(status_message)

      
        logging.info(f"URL: {url} - {status_message}")

        
        if 400 <= status_code < 500:
            print(f"ALERT: 4xx error encountered for URL: {url}")
            logging.warning(f"4xx error encountered for URL: {url}")
        elif 500 <= status_code < 600:
            print(f"ALERT: 5xx error encountered for URL: {url}")
            logging.error(f"5xx error encountered for URL: {url}")
        else:
            print("The website is UP and running.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking URL {url}: {e}")
        logging.error(f"Error checking URL {url}: {e}")

def monitor_urls(urls, interval=10):
    while True:
        print(f"\n{datetime.now()} - Monitoring URLs...")
        for url in urls:
            check_url_status(url)
        print(f"Waiting for {interval} seconds before the next check...")
        time.sleep(interval)


def exponential_backoff(retries, base_delay=1):
    return min(base_delay * (2 ** retries), 60) 


if __name__ == "__main__":
    monitor_urls(URLS)
            