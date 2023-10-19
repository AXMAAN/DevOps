"""
    This is  a quiz that tests the users knowlegde.
"""

# ask user for an input
fullName = input("Welcome to this quiz. \nPlease enter your name? ")
count = 0
print(f"welcome {fullName}")
first_question = input("What is the line that divides the earth into two called? ")
if first_question.lower() == "equator" :
     count += 1
     print(f"Congrats. The line that divides earth into two is called {first_question}.") 
     print("you have a point")
else:
     print("Incorrect. You can Give a try again. ") 

second_question = input("Which ocean is the biggest on Earth? ")
if second_question.lower() == "atlantic" :
     count += 1
     print(f"Congrats. The answer is: {second_question}.") 
     print(f"you have {count} points")
else:
     print("Incorrect. You can Give a try again. ") 

third_question = input("What is the pulling effect of an object called? ")
if third_question.lower() == "gravity" :
     count += 1
     print(f"Congrats. The answer is: {third_question}.") 
     print(f"you have {count} points")
else:
     print("Incorrect. You can Give a try again. ") 
fourth_question = input("Name the capital city of U.S.A? ")
if fourth_question.lower() == "new york" :
     count += 1
     print(f"Congrats. The answer is: {fourth_question}.") 
     print(f"you have {count} points")
else:
     print("Incorrect. You can Give a try again. ") 
fifth_question = input("Which country is the largest on earth? ")
if fifth_question.lower() == "russia" :
     count += 1
     print(f"Congrats. The answer is: {fifth_question}.") 
     print(f"you have {count}point")
else:
     print("Incorrect. You can Give a try again. ") 
sixth_question = input("Is a pajama the upper or lower clothing? ")
if sixth_question.lower() == "lower" :
     count += 1
     print(f"Congrats. The answer is: {sixth_question}.") 
     print(f"you have {count} point")
else:
     print("Incorrect. You can Give a try again. ") 

if count > 5:
     print(f"You're indeed genius. You got {count} points. I admire you.")
elif count >= 3:
     print(f"You try a little bit. You obtained {count} points.")
else:
     print(f"you failed terribly. How could you garner {count} points?")