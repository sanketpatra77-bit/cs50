name = input("your name? ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for s in name:
    if s not in vowels:
        print(s, end="")
