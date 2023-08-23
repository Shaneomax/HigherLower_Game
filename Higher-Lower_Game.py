import random

def higher_lower():
    number = random.randint(1, 100)
    guesses = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        guesses += 1

        if guess < number:
            print("The number is higher!")
        elif guess > number:
            print("The number is lower!")
        else:
            print("You guessed the number! You won in", guesses, "guesses.")
            break

if __name__ == "__main__":
    higher_lower()
