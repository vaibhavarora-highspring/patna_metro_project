import sqlite3
import csv

DB_PATH = "database/patna_metro.db"
CSV_FILE = "patna_metro_summary.csv"

def export_to_csv():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM route_summary")
    rows = cur.fetchall()

    headers = [desc[0] for desc in cur.description]

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    conn.close()
    print("CSV exported successfully:", CSV_FILE)

if __name__ == "__main__":
    export_to_csv()
