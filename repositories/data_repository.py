import sqlite3
import logging

DB_PATH = "data/lab_data.db"

class DataRepository:

    def _get_connection(self):
        return sqlite3.connect(DB_PATH)
    
    def create_table(self):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                               CREATE TABLE IF NOT EXISTS processed_data (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               record_id TEXT,
                               value REAL)""")
                conn.commit()
        except Exception as e:
            logging.error(f"Error creating table: {e}")
            raise
    
    def insert_records(self, records: list[dict]):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                for row in records:
                    cursor.execute(
                        "INSERT INTO processed_data (record_id, value) VALUES (?, ?)",
                        (row["id"], float(row["value"]))
                    )
                conn.commit()
        except Exception as e:
            logging.error(f"Error inserting records: {e}")
            raise

    def fetch_all(self):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM processed_data")
                return cursor.fetchall()
        except Exception as e:
            logging.error(f"Error fetching records: {e}")
            raise

    def clear(self):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM processed_data")
                conn.commit()
        except Exception as e:
            logging.error(f"Error clearing table: {e}")
            raise