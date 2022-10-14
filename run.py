from model_quest import Quiz
from quiz_questions import quiz_question_data
from brain import QuizBrain
import pyfiglet
from pyfiglet import figlet_format
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def title_start():
    """
    Print an welcome title customized by pyfilet and colorama, and
    an emoji ASCII art image from https://text-symbols.com/ascii-art/#all_cats
    """
    
    title = pyfiglet.figlet_format("Family Quiz", font="slant")
    print(f'{Fore.YELLOW}{title}')
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

    print(f'\n {Fore.YELLOW} Welcome to your Family Quiz.\n\n'
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
    question_text = question["question"]
    question_answer = question["correct_answer"]    
    new_question = Quiz(question_text, question_answer)   
    quiz_list.append(new_question)
 

quiz_new = QuizBrain(quiz_list)


while quiz_new.another_question():
    """
    check if the quiz still has questions
    """
    quiz_new.next_quest() 

title = pyfiglet.figlet_format("Congrats \n you complete \n Family Quiz", font="standard") 
print(f'{Fore.YELLOW}{title}') 
print(f"{Fore.CYAN}Your final score was: {quiz_new.score}/{len(quiz_list)}")


