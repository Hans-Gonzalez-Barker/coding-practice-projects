import random


def main():
    while True:
        choice = input(
            "Welcome to the simple integer guessing game. Would you like to play?"
            " Enter 'y' to accept and 'n' to reject: "
        )
        if choice == "y":
            guess()
        elif choice == "n":
            print("Ending game.")
            break
        else:
            print("Input not recognized, please try again.")
    print("Thank you for playing, goodbye.")


def guess():
    number = random.getrandbits(64)
    guesses = 0
    while True:
        guess = input("Enter your guess: ")
        if (not int(guess)) and (int(guess) < 0):
            print("Invalid input, please try again.")
            break
    print(f"{number} & {guesses}")


if __name__ == "__main__":
    main()
