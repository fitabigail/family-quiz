from model_quest import Quiz
from quiz_questions import quiz_question_data
from brain import QuizBrain



user_nickname = input("Chooce a nickname: ")
print(user_nickname)

quiz_list = []
"""
   Creating a question list of questing object using the class Quiz 
   for model question
"""
for question in quiz_question_data:      
    question_text = question["text"]
    question_answer = question["answer"]    
    new_question = Quiz(question_text, question_answer)   
    quiz_list.append(new_question)
 
  



quiz_new = QuizBrain(quiz_list)


while quiz_new.another_question():
    """
    chekhs if the qiuz still has questions
    """
    quiz_new.next_quest()

print("Congrats you have complete the Quiz!")  
print(f"Your final score was: {quiz_new.score}/{len(quiz_list)}")  





