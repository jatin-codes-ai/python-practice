# quiz_validator

print()

correct_answers = {'new delhi', 'pacific', 'peacock', 'hockey', 'tiger'}
answers = []
students_answers = set(answers)

print("Quiz Validator:\n")
answer1 = input("Question 1 - Capital of India? ").lower()
answers.append(answer1)
answer2 = input("Question 2 - Largest ocean? ").lower()
answers.append(answer2)
answer3 = input("Question 3 - National bird of India? ").lower()
answers.append(answer3)
answer4 = input("Question 4 - National sport of India? ").lower()
answers.append(answer4)
answer5 = input("Question 5 - National animal of India? ").lower()
answers.append(answer5)

right_answers = students_answers.intersection(correct_answers)
print(f"Correct: {right_answers}")

wrong_answers = students_answers - correct_answers
print(f"Wrong: {wrong_answers}")

print(f"Score: {len(right_answers)}/{len(correct_answers)}")

if len(right_answers) == len(correct_answers) :
    print("Status: Excellent!")
else : 
    print("Needs improvement.")

print()