# Define the four predetermined numbers
numbers = [10, 20, 30, 40]

# Initialize the total to zero
total = 0

# Loop until the total reaches 100
while total < 100:
    # Prompt the user for an input
    user_input = input("Please enter a number: ")
    
    # Try to convert the input to an integer
    try:
        user_input = int(user_input)
    except ValueError:
        # If the input is not a valid integer, continue the loop without printing anything
        continue
    
    # Check if the input is one of the four predetermined numbers
    if user_input in numbers:
        # Subtract the input from 100 and update the total
        total += user_input
        print(f"Subtracting {user_input} from 100. The remaining total is {100 - total}.")
    
# Print a message when the loop ends
print("You have reached the total of 100. The program ends.")
