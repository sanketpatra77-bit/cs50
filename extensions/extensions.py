def main():
    name = input("Enter your filename ").lower()

    if name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".jpg") or name.endswith(".jpeg"):
        print("image/jpeg")
    elif name.endswith(".txt"):
        print("text/plain")
    elif name.endswith(".zip"):
        print("application/zip")
    elif name.endswith(".png"):
        print("image/png")
    else:
        print("application/octet-stream")
main()