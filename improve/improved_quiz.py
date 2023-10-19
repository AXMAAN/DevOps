questions = [
    ("What is the line that divides the earth into two called?", "equator"),
    ("Which ocean is the biggest on Earth?", "atlantic"),
    ("What is the pulling effect of an object called?", "gravity"),
    ("Name the capital city of U.S.A?", "washington"),
    ("Which country is the largest on earth?", "russia"),
    ("Is a pajama the upper or lower clothing?", "lower")
]

count = 0
fullName = input("Welcome to this quiz.\nPlease enter your name: ")
print(f"Welcome {fullName}")

for question, answer in questions:
    user_answer = input(question + " ")
    if user_answer.lower() == answer:
        count += 1
        print(f"Congrats. The answer is {answer}. You have {count} point(s).")
    else:
        print("Incorrect. You can give it another try.")

if count >= 5:
    print(f"You're indeed a genius. You got {count} points. I admire you.")
elif count >= 3:
    print(f"You tried a little bit. You obtained {count} points.")
else:
    print(f"You failed terribly. How could you garner {count} points?")
