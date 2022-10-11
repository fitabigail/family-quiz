import re
import pyfiglet
from pyfiglet import figlet_format
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from model_quest import Quiz
from quiz_questions import quiz_question_data
from brain import QuizBrain




MSG = 'Welcome To FamilyQuiz'
FRONT = 'standard'


def title_start():
    """
    Print an welcome title customized by pyfilet and colorama, and
    an emoji ASCII art image from https://text-symbols.com/ascii-art/#all_cats
    """
    title = pyfiglet.Figlet(font=FRONT)    
    print(Fore.YELLOW + Style.BRIGHT + title.renderText(MSG))
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


def print_welcome_message():
    """
    Prints a  message to the terminal, and explain how many questions 
    have the QUIZ, category of the QUIZ, the level of Quiz.
    """
    quiz_rules = False

    print(f'\n {Fore.YELLOW}Welcome to your Family Quiz.\n\n'
          f'\n {Fore.CYAN}To keep you entertained, we are bringing you another Quiz.\n')

    while quiz_rules is False:
        choise = input(f'\n See here quiz {Fore.RED}rules. Choose {Fore.GREEN}(yes / no ): ')
        choise = choise.lower()
        if choise == 'yes':
            quiz_rules = True
            rules = (
                     '\n (1) Quiz Family complied a list of 10 questions'
                     ' for you to work you way through. \n\n '
                     '\n (2) They cover facts and myths'
                     ' from a range of topics including'
                     ' space, history, and geography. \n\n'
                     '\n (3) You will answer to each question '
                     ' by True or False statement. \n\n'
                     '\n (4) So, get ready , and sort out what is fact'
                     ' and what is fiction.\n\n'
                        
                        )
            print(rules)

        elif choise == 'no':
            quiz_rules = True
            print(f'\n  {Fore.CYAN}Start right now your quiz! \n')
        else:
            print(f"\n  {Fore.RED}Invalid answer, you must type either 'yes' or "
                    " 'no' \n")


title_start()
print_welcome_message()


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
    check if the qiuz still has questions
    """
    quiz_new.next_quest()

print("Congrats you have complete the Quiz!")  
print(f"{Fore.CYAN}Your final score was: {quiz_new.score}/{len(quiz_list)}")



