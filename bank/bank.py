def main():
    name = input("hello ").lower()

    if name.startswith("hello"):
        print("$0")
    elif name.startswith("h"):
        print("$20")
    else:
        print("$100")



main()