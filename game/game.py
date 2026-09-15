import random
while True:
    try:
        lavle = int(input("Lavle: "))
        if 0 < lavle:
            break
    except ValueError:
            pass


ans = random.randint(1, lavle)

while True:
    guess = int(input("Guess: "))
    if guess > ans:
          print("Too large!")
    elif guess > ans:
         print("Too small!")
    else:
        print("Just right!")
        break