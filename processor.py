import csv
import logging
from typing import List


def read_csv(file_path: str) -> List[dict]:
    try:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        logging.error(f"Error reading CSV: {e}")
        raise


def filter_data(data: List[dict], threshold: float) -> List[dict]:
    try:
        return [row for row in data if float(row["value"]) > threshold]
    except Exception as e:
        logging.error(f"Error filtering data: {e}")
        raise


def calculate_average(data: List[dict]) -> float:
    try:
        values = [float(row["value"]) for row in data]
        return sum(values) / len(values) if values else 0.0
    except Exception as e:
        logging.error(f"Error calculating average: {e}")
        raise