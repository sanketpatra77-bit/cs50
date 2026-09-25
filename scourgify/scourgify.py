import csv
import sys
def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r") as before:
            reader = csv.DictReader(before)

            with open(output_file, "w") as after:
                writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow({"first" : first, "last" : last, "house" : row["house"]})

    except FileExistsError:
        sys.exit(f"cood not read {input_file}")


main()