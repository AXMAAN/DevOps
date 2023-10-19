"""
    THIS CODE IS WRITTEN IN 10:17 PM OCTOBER 18TH 2023. IT ASKS USER SOME QUESTIONS
    AND COUNTS THE RESULTS.
"""


questions = [
    ("What is the line that divides the earth into two called?", "equator"),
    ("Which ocean is the biggest on Earth?", "atlantic"),
    ("What is the pulling effect of an object called?", "gravity"),
    ("Name the capital city of U.S.A?", "washington"),
    ("Which country is the largest on earth?", "russia"),
    ("Is a pajama the upper or lower clothing?", "lower")
]

count = 0
welcome_one = "########################################\n"
welcome_two = "###                                  ###\n"
welcome_third= "###     WELCOME  TO THIS QUIZ        ###\n"

fullName = input(F"{welcome_one}{welcome_two}{welcome_third}{welcome_two}{welcome_one} \nPlease enter your name: ")
print(f"Welcome Mr./Mrs {fullName}")

for question, answer in questions:
    attempt = 0
    while attempt < 3:
        user_answer = input(question + " ")
        if user_answer.lower() == answer:
            count += 1
            print(f"Congrats. The answer is {answer}. You have {count} point(s).")
            break
        else:
            print("Incorrect. Please try again.")
            attempt += 1
    if attempt == 3:
        print(f"Moving to the next question. You have {count} point(s).")
marks = count /6*100

if count > 5:
    print(f"You're indeed a genius. You got {marks:.2f}% marks. I admire you.")
elif count >= 3:
    print(f"You tried a little bit. You obtained {marks:.2f}% marks.")
else:
    print(f"You failed terribly. How could you garner {marks:.2f}% marks?")
