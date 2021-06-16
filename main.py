from question_model import Question
from data import get_data
from quiz_brain import QuizBrain
from ui import Quiz_UI

question_bank = []
for question in get_data():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

if __name__ == "__main__":
    quiz = QuizBrain(question_bank)
    quiz_ui = Quiz_UI(quiz)

