import logging
import argparse
from processor.csv_processor import read_csv, filter_data, calculate_average, write_csv
from services.data_service import DataService

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    service = DataService()

    parser = argparse.ArgumentParser(description="Process laboratory data.")
    parser.add_argument(
        "--threshold",
        type=float,
        default = 15,
        help="Threshold value for filtering"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/sample_data.csv",
        help="Path to input CSV file"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List stored records from database"
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear all records from database"
    )

    args = parser.parse_args()

    if args.list:
        records = service.list_records()

        print("\nStored Records:")
        for row in records:
            print(f"ID: {row[0]} | Record ID: {row[1]} | Value: {row[2]}")
        return

    if args.clear:
        service.clear_records()
        print("All records have been deleted.")
        return

    logging.info(f"Starting data processing with threshold {args.threshold}")

    data = read_csv(args.input)
    filtered = filter_data(data, args.threshold)

    service.save_records(filtered)
    
    average = calculate_average(filtered)

    output_path = "data/filtered_output.csv"
    write_csv(output_path, filtered)

    print("Filtered Data:")
    for row in filtered:
        print(row)
    
    print(f"\nAverage value: {average}")
    print(f"Filtered data saved to {output_path}")

if __name__ == "__main__":
    main()