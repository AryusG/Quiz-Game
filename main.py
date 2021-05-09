from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# TODO Create a question model for each key value pair in question_data
for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

# TODO go through questions, checking if correct and checking if at end of quiz
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"\nYou've completed the quiz!\n"
      f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")