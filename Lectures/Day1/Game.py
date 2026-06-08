number = 35
count = 0
while (count < 3):
    guess = int(input("Guess the number:"))
    count += 1
    if(guess < number):
        print("Too low!")
    elif(guess > number):
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break