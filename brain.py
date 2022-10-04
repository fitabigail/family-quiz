class QuizBrain:
    def __init__(self, quest_list):
        self.quest_num = 0
        self.list = quest_list

    def another_question(self):
        """
        define function for another question
        """
        return self.quest_num < len(self.list)

    def next_quest(self):
        active_quest = self.list[self.quest_num]
        self.quest_num += 1
        input(f"Q.{self.quest_num}: {active_quest.text} (True/False):")

