import re
def main():
    plate = input("Plates: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(plate):
    valid =
    if 2 <= len(plate) <= 6 and (plate[0:].isalpha() or plate[:2].isalpha()) and (plate[2:].isdigit() or plate[3:].isdigit() or plate[4:].isdigit() or plate[5:].isdigit() or plate[6:].isdigit()) and valid == plate:
         return True

    

    
main()

""" 
       for char in plate:
            if char[2:].isdigit():
                if char[3:].isalpha():
                    return False
                return True
         return False
"""