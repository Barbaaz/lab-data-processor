import sqlite3
import logging

DB_PATH = "data/lab_data.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS processed_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_id TEXT,
            value REAL
        )
        """)

        conn.commit()
        conn.close()
        logging.info("Database table ensured.")
    except Exception as e:
        logging.error(f"Error creating table: {e}")
        raise

def insert_records(records: list[dict]):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        for row in records:
            cursor.execute(
                "INSERT INTO processed_data (record_id, value) VALUES (?, ?)",
                (row["id"], float(row["value"]))
            )
        
        conn.commit()
        conn.close()
        logging.info(f"{len(records)} records inserted into database.")
    except Exception as e:
        logging.error(f"Error inserting records: {e}")
        raise

def fetch_all_records() -> list[tuple]:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM processed_data")
        rows = cursor.fetchall()

        conn.close()
        return rows
    except Exception as e:
        logging.error(f"Error fetching records: {e}")
        raise