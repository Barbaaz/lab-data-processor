import csv
import logging

def read_csv(file_path: str) -> list[dict]:
    try:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]    
    except Exception as e:
        logging.error(f"Error reading CSV: {e}")
        raise

def filter_data(data: list[dict], threshold: float) -> list[dict]:
    filtered = []
    for row in data:
        try:
            value = float(row["value"])
            if value > threshold:
                filtered.append(row)
        except (ValueError, KeyError):
            logging.warning(f"Invalid row skipped: {row}")
    return filtered


def calculate_average(data: list[dict]) -> float:
    try:
        values = [float(row["value"]) for row in data]
        return sum(values) / len(values) if values else 0.0
    except Exception as e:
        logging.error(f"Error calculating average: {e}")
        raise

def write_csv(file_path: str, data: list[dict]) -> None:
    try:
        if not data:
            logging.warning("No data to write.")
            return
        with open(file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"Data written successfully to {file_path}")
    except Exception as e:
        logging.error(f"Error writing CSV: {e}")
        raise