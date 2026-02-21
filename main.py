import logging
import argparse
from processor import read_csv, filter_data, calculate_average, write_csv


logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
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

    args = parser.parse_args()

    logging.info(f"Starting data processing with threshold {args.threshold}")

    data = read_csv(args.input)
    filtered = filter_data(data, args.threshold)
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