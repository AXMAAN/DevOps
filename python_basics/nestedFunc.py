def input_and_display():
  # nested function that receives input from the user
  def get_input():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last
  # call the nested function and store the returned values
  first, last = get_input()
  # display the inputs
  print("You entered: " + first + " " + last)

# call the outer function
input_and_display()
