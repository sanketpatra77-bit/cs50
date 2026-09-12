import inflect

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

s = inflect.engine()

print(f"\nAdieu, adieu, to {s.join(names)}")