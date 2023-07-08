import json

with open("files/bonus11.json", 'r') as file:
    content = file.read()

data = json.loads(content)   # to load the content as list to extract it


score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}-{alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_answer"] = user_choice
    if question["user_answer"] == question["correct_answer"]:
        score = score + 1
        result = "Correctly Answered"
    else:
        result = "Wrongly Answered"

for index, question in enumerate(data):
    message = f"{result} for Question:{index + 1} - Your answer: {question['user_answer']}, Correct answer: {question['correct_answer']}"
    print(message)

print(f"Score: {score}/{len(data)}")
