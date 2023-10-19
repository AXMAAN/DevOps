import sys

def main():
    calc()

def calc():
    try:
        first_number = float(input("Please Enter the first number for the calculation: "))
        the_sign = input("Please Enter an operation (+, -, *, /): ")
        second_number = float(input("Please Enter the second number for the calculation: "))

        if the_sign == "-":
            print(f"The result is: {first_number - second_number}")
        elif the_sign == "+":
            print(f"The result is: {first_number + second_number}")
        elif the_sign == "/":
            if second_number != 0:
                print(f"The result is: {first_number / second_number}")
            else:
                print("Division by zero is not allowed.")
        elif the_sign == "*":
            print(f"The result is: {first_number * second_number}")
        else:
            print("Please enter a valid expression.")

        the_prompt()

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        calc()

def the_prompt():
    while True:
        the_prompt_input = input("Would you like to continue? \nY for Yes and \nN for No: ")
        if the_prompt_input.lower() == "y":
            calc()
        elif the_prompt_input.lower() == "n":
            print("Thanks for the calculation. Goodbye.")
            sys.exit()
        else:
            print("Please enter a valid option (Y/N).")

if __name__ == "__main__":
    main()
