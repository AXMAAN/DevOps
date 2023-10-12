def main():
    plate = input("Plates: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate[:2].isalpha():
         return True
    if plate[0:].isalpha() or plate[2:].isdigit() or plate[3:].isdigit() or plate[4:].isdigit() or plate[5:].isdigit() or plate[6].isdigit():
                if not plate.isalpha() or not plate[2:].isdigit():
                    return True
                return True
    

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