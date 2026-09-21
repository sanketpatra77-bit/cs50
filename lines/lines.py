import sys
def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        count = 0
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue

                count += 1
        print(count)

    except FileNotFoundError:
        sys.exit("File dose not found")

main()
