import re
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matchs = re.fullmatch(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if not matchs:
        return False

    for group in matchs.groups():
        if not 0 <= int(group) <= 255:
            return False
    return True

if __name__ == "__main__":
    main()