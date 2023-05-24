class QuizBrain:
    def __init__(self, q_list: list):
        """create a new QuizBrain class with given question list"""
        self.question_number = 0
        self.questin_list = q_list
        # getting len of the list in initialize function give us less time complexity
        self.len_questin_list = len(q_list)
        self.score = 0


    @property    
    def still_has_question(self):
        """return True if there is question remaining otherwise False"""
        return self.question_number < self.len_questin_list
    
    def next_question(self):
        """ask the user a new question from the list of questions"""
        question = self.questin_list[self.question_number] # getting a question
        self.question_number += 1
        # asking question
        answer = input(f"Q.{self.question_number}: {question.text} (True|False)?: ")
        self.check_answer(question, answer)
            
    def check_answer(self, question, answer):
        if question.check_answer(answer): # checking the answer
            print("excellent job!")
            self.score += 1
        else:
            print(f"wrong answer! the correct answer is {question.answer}")
        print(f"your corrent score is {self.score}/{self.question_number} \n")
