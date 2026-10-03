import validators
def main():
    email = input("Enter your email address: ")
    if validate(email):
        print("Valid")
    else:
        print("Invalid")

def validate(email):
    return validators.email(email)

if __name__ == "__main__":
    main()