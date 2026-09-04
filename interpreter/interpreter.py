x ,y ,z = input("what is your x ,y ,z? ").split()

if y == "+":
    result = int(x) + int(z)
elif y == "-":
    result = int(x) - int(z)
elif y == "*":
    result = int(x) * int(z)
elif y == "/":
    result = int(x) / int(z)
print(f"{result:.1f}")