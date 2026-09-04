def convert(time):
    hours, minutes = time.split(":")
    result = int(hours) + int(minutes) / 60
    return result

def main():
    time = convert(input("what time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

main()