import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")


    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            table = list(reader)

        header = table[0]
        rows = table[1:]

        print(tabulate(rows, header, tablefmt="grid"))

    except FileExistsError:
        sys.exit(f"Could not find {filename}")

main()