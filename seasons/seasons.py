from datetime import date
import inflect
import sys

def get_minutes(s):
    a = date.fromisoformat(s)
    b = date.today()
    return ((b - a).days * 24) * 60

p = inflect.engine()
def to_words(n):
    w = p.number_to_words(n, andword = "") + " minutes"
    return w.capitalize()

def main():
    s = input("Date of Birth: ")
    try:
        minutes = get_minutes(s)
    except ValueError:
        sys.exit("Invalid Date")
    print(to_words(minutes))

if __name__ == "__main__":
    main()