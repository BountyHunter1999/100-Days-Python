from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # for key, value in question.items():
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)
# print(quiz.still_has_questions())
while quiz.still_has_questions():
    quiz.next_question()
    print("")

print(f"Your final score was: {quiz.score} / {len(question_bank)}")
# print(quiz.question_number) 12
