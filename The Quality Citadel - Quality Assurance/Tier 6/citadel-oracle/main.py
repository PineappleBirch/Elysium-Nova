import requests
import configparser
import time
import schedule


def read_config():
    """
    Reads the configuration file to get target URLs.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['TARGETS']


def health_check(url):
    """
    Performs a simple health check on a given URL.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"[{time.ctime()}] CHECK PASSED: {url} is UP and running.")
        else:
            print(f"[{time.ctime()}] CHECK FAILED: {url} is DOWN. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{time.ctime()}] CHECK FAILED: {url} is DOWN. Error: {e}")


# --- Main execution block for continuous monitoring ---
if __name__ == "__main__":
    targets = read_config()
    interval = 1

    # Scheduling the health_check function to run every 1 minute
    # For a real-world scenario, you might change this to every 5 or 10 minutes.
    schedule.every(interval).minutes.do(health_check, url=targets['main_site'])

    print("--- Starting continuous monitoring... Press CTRL+C to stop. ---")

    # Running one check immediately at the start
    health_check(targets['main_site'])

    # Infinite loop to keep the script running and executing scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(1)