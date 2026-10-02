import re
def main():
    print(parse(input("Enter URL: ")))

def parse(s):
    match = re.search(r"src=\"https?://www\.youtube\.com/embed/(\w+)\"", s)
    if match:
        return "https://youtu.be/" + match.group(1)
if __name__ == "__main__":
    main()