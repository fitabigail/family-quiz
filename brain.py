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
        user_answer = input(f"Q.{self.quest_num}: {active_quest.text} (True/False):")
        self.keep_score(user_answer, active_quest.answer)

    def  keep_score(self, user_answer, correct_answer):
        """
        Print user score  after each question
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct")
            
        else:
            print("Inccorect answer.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.quest_num}")
        print("\n")




