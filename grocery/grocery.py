items = {}

while True:
    try:
        item = input("enter item: ").lower()

        
    except EOFError:
        break

    if item in items:
        items[item] += 1

    else:
        items[item] = 1

for item in sorted(items):
    print(f"{items[item]} {item.upper()}")

