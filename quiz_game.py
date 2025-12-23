questions = ("how many elements in periodic table?",
             "which animal lays the target eggs?",
             "what is the most abundant gas in earth's atmosphere?",
             "how many bones are there in human body?",
             "which planet in the solar system is the hottest?")

options = ( ("A. 116","B. 117", "C. 118","D. 119"),
            ("A. whale ","B. crocodile", "C. elephant","D. Ostrich"),
            ("A. Nitrogen","B. Oxygen", "C. Carbon-dioxide","D. Hydrogen"),
            ("A. 206","B. 207", "C. 208","D. 209"),
            ("A. Mercury","B. venus", "C. Earth","D. Mars")
)

answers = ("C", "D", "A", "A", "B")
guesses = []
question_num = 0
score = 0

for question in questions:
    print ("---------------")
    print (question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print ("Correct!")
    else:
        print ("Wrong!")
        print (f"{answers[question_num]} is the correct answer!")

    question_num += 1

print("-------------------------")
print("--------RESULTS----------")
print("-------------------------")

print ("answers:", end = " ")
for answer in answers:
    print (answer, end = " ")
print ()

print ("guesses:", end = " ")
for guess in guesses:
    print (guess, end = " ")
print ()

score = int(score / len(questions)* 100)

print (f"your score is: {score}%")