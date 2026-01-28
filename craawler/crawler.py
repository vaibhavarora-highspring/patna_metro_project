import requests
import logging
import os

URL = "https://www.mypatnametro.com/"

def fetch_html():
    logging.info("Starting HTML fetch")

    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()

        os.makedirs("data", exist_ok=True)

        with open("data/patna_metro_raw.html", "w", encoding="utf-8") as file:
            file.write(response.text)

        logging.info("HTML saved successfully")
        print("HTML downloaded and saved successfully")

    except Exception as e:
        logging.error(f"Error fetching HTML: {e}")
        print("Failed to fetch website")

if __name__ == "__main__":
    fetch_html()
