def main():

    print(
        "Welcome to the temperature and distance converter! We convert between Fahrenheit"
        " and Celsius, as well as miles and kilometers."
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
            value = input_validation("distance", "kilometers")

            answer = round(value * 0.621371, 2)

            print(f"Your distance is {answer} mile(s).")

            status = True
        elif choice == "m":
            value = input_validation("distance", "miles")

            answer = round(value / 0.621371, 2)

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
            value = input_validation("temperature", "celsius")

            answer = round((value * (9 / 5)) + 32, 2)

            print(f"Your temperature is {answer} fahrenheit.")

            status = True
        elif choice == "f":
            value = input_validation("temperature", "fahrenheit")

            answer = round((value - 32) * (5 / 9), 2)

            print(f"Your temperature is {answer} celsius.")

            status = True
        else:
            print("Input not recognized, please try again.")


def input_validation(theme, unit):
    while True:
        try:
            temp = float(input(f"Enter {theme} in {unit}: "))
            return temp
        except ValueError:
            print("Invalid input, must be a valid number, try again.")


if __name__ == "__main__":
    main()
