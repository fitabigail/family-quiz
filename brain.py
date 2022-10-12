import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
       


class QuizBrain:
    def __init__(self, quest_list):
        self.quest_num = 0
        self.score = 0
        self.list = quest_list
     
    def another_question(self):
        """
        define function for another question
        """
        return self.quest_num < len(self.list)
      
    def next_quest(self):
        """
        Display the next question with a number
        """
        active_quest = self.list[self.quest_num]
        self.quest_num += 1 
        print("-------------------\n") 
        print(f"\n Q.{self.quest_num}: {active_quest.text}  ")          
        user_answer = input(f"\n Your answer (True/False):  ")       
        self.keep_score(user_answer, active_quest.answer)
        
    def keep_score(self, user_answer, correct_answer):
        """
        Print user score  after each question
        """
        while user_answer.lower() not in ['true','false']:
            print(f" \n {Fore.RED}Sorry not a valid answer")
            user_answer = input(f" \n Please insert another answer (True/False): ")
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f" \n {Fore.GREEN}Correct answer")
        else:
            print(f" \n {Fore.RED}Inccorect answer.")
        print(f" \n {Fore.YELLOW}The correct answer was: {correct_answer}.")
        print(f" \n Your current score is {Fore.BLUE}{self.score}/{self.quest_num}")
        print("\n")
      


