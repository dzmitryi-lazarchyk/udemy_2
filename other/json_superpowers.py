import json


with open('../files/questions.json', 'r') as file:
    content = file.read()
    # data1 = json.load(file)

data = json.loads(content)
# print(data)
score = 0

for question in data:
    #Program asks question
    print(question["question_text"])
    #Gives alternatives
    for alternative in question['alternatives']:
        print(f"{question['alternatives'].index(alternative)+1} - {alternative}")

    user_choice = int(input("Enter number of the right answer:"))
    question['user_choice'] = user_choice
    with open('../files/questions.json', 'w') as file:
        json.dump(data, file)
for index, question in enumerate(data):
    user_answer = question['user_choice']
    correct_answer = question['correct_answer']

    if user_answer == correct_answer:
        msg = "Correct answer".upper()
        score += 1
    else:
        msg = "Incorrect answer".upper()
    print(f"{index+1}.{msg}. User answer:{user_answer}."
          f" Correct answer:{correct_answer}")
print(f"Score:{score}/{len(data)}")







