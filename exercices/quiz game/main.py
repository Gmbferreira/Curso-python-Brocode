questions =  ("How many elements are in the periodic table?: ",
             "What is the capital of France?: ",
             "What is the largest planet in our solar system?: ",
             "What is the chemical symbol for gold?: ",
             "How many bones are in the human body?: ")

options = (("A) 118", "B) 119", "C) 120", "D) 121"),
           ("A) London", "B) Paris", "C) Rome", "D) Berlin"),
           ("A) Jupiter", "B) Saturn", "C) Uranus", "D) Neptune"),
           ("A) Ag", "B) Au", "C) Al", "D) As"),
           ("A) 206", "B) 208", "C) 210", "D) 212"))

answers = ("A", "B", "A", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print ("--------------------------")
    print (question)
    for option in options[question_num]:
        print (option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print ("CORRECT!")
    else:
        print ("INCORRECT!")
        print (f"{answers[question_num]} is the correct answer.")

    question_num += 1

print ("--------------------------")
print ("RESULTS")
PRINT ("--------------------------")

PRINT("Answers: ", end="")
for answer in answers:
    print (answer, end=" ")
print()

print ("Guesses: ", end="")
for guess in guesses:
    print (guess, end=" ")
print()

score = int(score / len(questions) * 100)
print (f"Your score is: {score}%")
