import random

# Generate a random number to be guessed
number = random.randint(0, 100)

print("Guess a magic number between 0 and 100")

guess = -1    # guess被初始化为-1，为了避免将它初始化为一个0到100之间的数字，因为那可能就是要猜测的数字
while guess != number:
    # Prompt the user to guess the number
    guess = eval(input("Enter your guess: "))


    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")