import re

def main():
    print(convert(input("Hours: ")))

    
def convert(s):
    match = re.search(r"^(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)$", s)
    if not match:
        return ("invalid time")

    h1, m1, p1, h2, m2, p2 = match.groups()

    h1, m1 = int(h1), int(m1)
    h2, m2 = int(h2), int(m2)

    if not (0 <= h1 <= 12 and 0 <= m1 <= 59):
        return ("invalid time")
    if not (0 <= h2 <= 12 and 0 <= m2 <= 59):
        return ("invalid time")

    def to_24(h, m, p):
        if p == "AM":
            if h == 12:
                h = 0
        else:
            if h != 12:
                h += 12
        return f"{h:02}:{m:02}"

    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"

if __name__ == "__main__":
    main()