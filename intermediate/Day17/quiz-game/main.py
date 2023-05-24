from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
# filling the question bank
for data in question_data:
    question_bank.append(
        Question(data['text'], data['answer'])
    )
# creating a new quiz by the question bank
quiz = QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()
    