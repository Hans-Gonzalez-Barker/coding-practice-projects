import random


def input_validation():
    while True:
        try:
            temp = int(input("Enter your guess between -500 and 500: "))
            return temp
        except ValueError:
            print("Invalid input, must be a valid integer, try again.")


def guess():
    number = random.randint(-500, 500)
    guesses = 0
    check = False
    while not check:
        guess = input_validation()
        if guess > 500 or guess < -500:
            print("Invalid input, guess is out of range, please try again. ")
        elif guess == number:
            print("You got it!")
            guesses += 1
            check = True
        elif guess < number:
            print("Too low, try again.")
            guesses += 1
        elif guess > number:
            print("Too high, try again.")
            guesses += 1
    print(f"The number was: {number} and it took {guesses} guesses.")


def main():
    while True:
        choice = input(
            "Welcome to the simple integer guessing game. Would you like to play (again)?"
            " Enter 'y' to accept and 'n' to reject: "
        ).lower()
        if choice == "y":
            guess()
        elif choice == "n":
            print("Ending game.")
            break
        else:
            print("Input not recognized, please try again.")
    print("Thank you for playing, goodbye.")


if __name__ == "__main__":
    main()
