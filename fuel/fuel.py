while True:
    try:
        function = input("function: ")
        x, y = function.split("/")
        x = int(x)
        y = int(y)

        if x > y:
            continue
        s = round(x / y * 100)
        break

    except ValueError:
        continue
    except ZeroDivisionError:
        continue

if s <= 1:
    print("E")
elif s >= 99:
    print("F")
else:
    print(f"{s}%")