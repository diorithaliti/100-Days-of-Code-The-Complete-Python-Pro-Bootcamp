from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for each in question_data:
    q = each["text"]
    a = each["answer"]
    new_question = Question(q, a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


