"""
    This code is meant for pratical purposes. It was started in 05:32 pm on  18th October 2023.
    The code is a calculator that has to accept mathematical calculations.
"""
import sys

def main():
    
    calc()
    

def calc():
    first_number = int(input("Please Enter a number for the calculation: "))
    the_sign = input("Please Enter a +-*/ etc: ")
    second_number = int(input("Please Enter a second number for the calculation: "))

    if the_sign == "-" :
        print(first_number - second_number)
    elif the_sign == "+" :
        print(first_number + second_number)
    elif the_sign == "/" :
        print(first_number / second_number)
    elif the_sign == "*" :
        print(first_number * second_number)
    else:
        print("Please enter a valid expression. ")
        calc()
        
    def the_prompt():
        the_prompt = input("Would you like to continue? \nY for Yes and \nN for No: ")
        if the_prompt == "Y" or the_prompt == "y":
            calc()
        elif the_prompt == "N" or the_prompt == "n" :
            print("Thanks for the calculation. Goodbye.")
            sys.exit()
        else:
            print("Please enter a valid letter: ")
            the_prompt()
    the_prompt()
        

main()



    
        
