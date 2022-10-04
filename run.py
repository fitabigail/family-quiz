from model_quest import Quiz
from quiz_questions import quiz_question_data

quiz_list = []
"""
   Creating a question list of questing object using the class Quiz for model question
"""
for question in quiz_question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Quiz(question_text, question_answer)
    quiz_list.append(new_question)


print(quiz_list)





