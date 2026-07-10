"""
CSV Data Analyzer
Reads a CSV file and prints statistical summaries.
"""

import csv
import sys
from pathlib import Path


def read_csv(filename):
    """Read a CSV file and return a list of dictionaries."""

    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    if not data:
        raise ValueError("The CSV file is empty.")

    return data


def detect_numeric(data):
    """Return a list of numeric columns."""

    numeric_columns = []

    for column in data[0].keys():
        is_numeric = True

        for row in data:
            try:
                float(row[column])
            except ValueError:
                is_numeric = False
                break

        if is_numeric:
            numeric_columns.append(column)

    return numeric_columns


def calculate_stats(values):
    """Return count, sum, mean, min and max."""

    count = len(values)
    total = sum(values)
    mean = total / count
    minimum = min(values)
    maximum = max(values)

    return {
        "count": count,
        "sum": total,
        "mean": mean,
        "min": minimum,
        "max": maximum
    }


def format_report(data, filename):
    """Print the analysis report."""

    numeric_columns = detect_numeric(data)

    print("=" * 60)
    print("CSV ANALYSIS REPORT")
    print("=" * 60)
    print(f"File: {filename}")
    print(f"Total rows: {len(data)}")
    print(f"Total columns: {len(data[0])}")

    print("\nNUMERIC COLUMNS:")
    print("-" * 60)

    if not numeric_columns:
        print("No numeric columns found.")

    for column in numeric_columns:
        values = [float(row[column]) for row in data]

        stats = calculate_stats(values)

        print(f"\nColumn: {column}")
        print(f" Count : {stats['count']}")
        print(f" Sum   : {stats['sum']:.2f}")
        print(f" Mean  : {stats['mean']:.2f}")
        print(f" Min   : {stats['min']:.2f}")
        print(f" Max   : {stats['max']:.2f}")

    print("\nNON-NUMERIC COLUMNS:")
    print("-" * 60)

    for column in data[0].keys():
        if column not in numeric_columns:
            values = [row[column] for row in data]
            unique_values = len(set(values))

            print(
                f"Column: {column} → {len(values)} values, {unique_values} unique"
            )

    print("=" * 60)


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter CSV filename: ").strip()

    try:
        data = read_csv(filename)
        format_report(data, filename)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()