def main():

    print(
        "Welcome to the temperature and distance converter! We convert between Fahrenheit"
        "and Celsius, as well as miles and kilometers."
    )

    leave = False
    while not leave:
        choice = input(
            "Would you like to convert temperature or distance? Enter 't' for"
            " temperature, 'd' for distance, or 'q' to quit: "
        ).lower()

        if choice == "t":
            temperature_converter()
        elif choice == "d":
            distance_converter()
        elif choice == "q":
            leave = True
        else:
            print("Input not recognized, please try again.")

    print("Goodbye!")


def distance_converter():
    status = False
    while not status:
        choice = input(
            "Enter 'k' for kilometers to miles, or 'm' for miles to kilometers: "
        ).lower()
        if choice == "k":
            while True:
                try:
                    d = float(input("Enter distance in kilometers: "))
                    break
                except ValueError:
                    print("Invalid input, must be a valid number, try again.")

            answer = round(d * 0.621371)

            print(f"Your distance is {answer} mile(s).")

            status = True
        elif choice == "m":
            while True:
                try:
                    d = float(input("Enter distance in miles: "))
                    break
                except ValueError:
                    print("Invalid input, must be a valid number, try again.")

            answer = round(d / 0.621371)

            print(f"Your distance is {answer} kilometer(s).")

            status = True
        else:
            print("Input not recognized, please try again.")


def temperature_converter():
    status = False
    while not status:
        choice = input(
            "Enter 'c' for celsius to fahrenheit, or 'f' for fahrenheit to celsius: "
        ).lower()
        if choice == "c":
            while True:
                try:
                    temp = float(input("Enter temperature in celsius: "))
                    break
                except ValueError:
                    print("Invalid input, must be a valid number, try again.")

            answer = round((temp * (9 / 5)) + 32)

            print(f"Your temperature is {answer} fahrenheit.")

            status = True
        elif choice == "f":
            while True:
                try:
                    temp = float(input("Enter temperature in fahrenheit: "))
                    break
                except ValueError:
                    print("Invalid input, must be a valid number, try again.")

            answer = round((temp - 32) * (5 / 9))

            print(f"Your temperature is {answer} celsius.")

            status = True
        else:
            print("Input not recognized, please try again.")


if __name__ == "__main__":
    main()
