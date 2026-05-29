# Quiz game

print()

questions = {
    "What is capital of India?": "delhi",
    "What is 15 × 4?": "60",
    "What language are you learning?": "python",
    "What does PMO stand for?": "porn", 
    "What is your rank?": "d"
}

total = len(questions)
score = 0

for key, value in questions.items() :
    print(questions[key])
    ip = input("Enter your answer: ").lower
    if ip == questions[value] :
        score += 1
        print("Correct!")
    else :
        print(f"Wrong. The answer was {questions[value]}]")

print(f"Your score: {score}/{total}.")

percentage = (score/total)*100

print(f"Percentage: {percentage}%")
