from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

quiz = QuizInterface()
# while quiz.still_has_question():
#     quiz.next_question()

print("You have completed the quiz.")
print(f"Your total score is {quiz.score}/{quiz.question_number}")