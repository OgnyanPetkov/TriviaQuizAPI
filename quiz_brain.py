import html


class QuizBrain:
    def __init__(self, question_list):
        self.q_num = 0
        self.score = 0
        self.q_list = question_list
        self.current_question = None

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def next_q(self):
        self.current_question = self.q_list[self.q_num]
        self.q_num += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.q_num}:{q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
