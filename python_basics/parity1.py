def main():
    x = int(input("Type a number: "))
    is_even(x)

def is_even(n):
    if n % 2 == 0:
        print("X: is indeed an even number. ")
    else: 
        print("X: is odd.")

main()