import logging
from bs4 import BeautifulSoup

HTML_FILE = "data/patna_metro_raw.html"

def extract_stations():
    logging.info("Starting station extraction")

    try:
        with open(HTML_FILE, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")

        stations = set()

        # Generic approach: find all text that looks like station names
        for tag in soup.find_all(["h1", "h2", "h3", "p", "li", "span"]):
            text = tag.get_text(strip=True)

            if "station" in text.lower():
                stations.add(text)

        stations = sorted(stations)

        logging.info(f"Extracted {len(stations)} station-related entries")

        return stations

    except Exception as e:
        logging.error(f"Error parsing stations: {e}")
        return []

if __name__ == "__main__":
    stations = extract_stations()

    print("\nExtracted Station-related Text:")
    print("-" * 40)
    for s in stations:
        print(s)
