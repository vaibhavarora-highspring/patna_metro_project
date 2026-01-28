import sqlite3
import os

DB_PATH = "database/patna_metro.db"

def get_connection():
    os.makedirs("database", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS route_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_station TEXT,
            end_station TEXT,
            stations_between TEXT,
            distance REAL,
            duration INTEGER,
            interchanges INTEGER,
            fare INTEGER,
            first_train TEXT,
            last_train TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_summary(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO route_summary (
            start_station, end_station, stations_between,
            distance, duration, interchanges, fare,
            first_train, last_train
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["start"],
        data["end"],
        ", ".join(data["stations_between"]),
        data["distance"],
        data["duration"],
        data["interchanges"],
        data["fare"],
        data["first_train"],
        data["last_train"]
    ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database ready")
