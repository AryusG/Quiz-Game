# TODO asking the questions

# TODO checking if answer was correct

# TODO check if we at the end of the quiz

class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0

    def still_has_questions(self):
        """Return Boolean"""
        return len(self.questions_list) > self.question_number

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True or False?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print(f"Correct!")
        else:
            print(f"Incorrect!")
        print(f"The correct answer was: {answer}\n"
              f"Your current score is: {self.score}/{self.question_number}")