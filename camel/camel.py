name = input("what? ")
for s in name:
    if s.isupper():
        print("_" + s.lower(), end="")
    else:
        print(s, end="")