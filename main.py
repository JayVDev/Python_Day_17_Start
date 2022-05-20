from data import question_data
from question_model import Question

# Variables
questions_bank = []

for dic in question_data:
    questions_bank.append(Question(dic["text"], dic["answer"]))

print(questions_bank)