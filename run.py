import re
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from model_quest import Quiz
from quiz_questions import quiz_question_data
from brain import QuizBrain



MSG = 'Welcome To FamilyQuiz'
FRONT = 'standard'


def print_welcome_msg():
    f = pyfiglet.Figlet(font=FRONT)    
    print(Fore.YELLOW + Style.BRIGHT + f.renderText(MSG))
    print(emoji_display)



emoji_display = \
"""
░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████

"""

print_welcome_msg()
"""
def user_name():
    while True:
        user_nickname = input("Chooce a nickname: ")
        if not user_nickname:
            print("The answer given does not compute!! Try again")
        continue
        else:
            break

print(user_nickname, " welcome to the Family Quiz.")
    
user_name(user_nickname)  
"""
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
print(f"{Fore.CYAN}Your final score was: {quiz_new.score}/{len(quiz_list)}")  





