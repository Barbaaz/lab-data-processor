import logging
from processor import read_csv, filter_data, calculate_average


logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    file_path = "data/sample_data.csv"
    threshold = 15

    logging.info("Starting data processing")

    data = read_csv(file_path)
    filtered = filter_data(data, threshold)
    average = calculate_average(filtered)

    logging.info(f"Filtered records: {len(filtered)}")
    logging.info(f"Average value: {average}")

    print("Filtered Data:")
    for row in filtered:
        print(row)

    print(f"\nAverage value: {average}")


if __name__ == "__main__":
    main()