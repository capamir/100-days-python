class Question:
    def __init__(self, text, answer):
        """create a new Question with the given text and answer"""
        self.text = text
        self.answer = answer

    def check_answer(self, answer):
        """Check answer is correct or wrong"""
        return True if self.answer.lower() == answer.lower() else False
  