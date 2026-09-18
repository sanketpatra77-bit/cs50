def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    
    percentage = x / y * 100    # ← division আগে, y=0 হলে এখানেই ZeroDivisionError আসবে
    
    if x > y:
        raise ValueError
    
    return round(percentage)
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()