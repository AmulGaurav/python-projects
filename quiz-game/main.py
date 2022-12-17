from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz_1 = QuizBrain(question_bank)

while quiz_1.still_has_questions():
    quiz_1.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz_1.score}/{len(question_bank)}")