total = 0
while total < 50:
    coin = int(input("payment: "))
    if coin == 25:
        total += 25
    elif coin == 10:
        total += 10
    elif coin == 5:
        total += 5

    if total < 50:
        print(f"Amount due: {50 - total}")

print(f"Change owed: {total - 50}")