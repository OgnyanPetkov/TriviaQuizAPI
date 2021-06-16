from tkinter import *
from quiz_brain import QuizBrain

bg_color = "#375362"


class Quiz_UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz trivia")
        self.window.config(padx=20, pady=20, bg=bg_color)

        self.score = Label(bg=bg_color, fg="white", font=("Arial", 20, "italic"), text=f"Score:{self.quiz.score}")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.trivia_q = self.canvas.create_text((150, 125),
                                                text=f"Question",
                                                fill=bg_color,
                                                font=("Arial", 20, "italic"),
                                                width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        tick = PhotoImage(file="images/true.png")
        cross = PhotoImage(file="images/false.png")
        self.true_button = Button(image=tick, highlightthickness=0, relief=FLAT, borderwidth=0,
                                  command=self.answer_true)
        self.true_button.grid(row=2, column=1)
        self.false_button = Button(image=cross, highlightthickness=0, relief=FLAT, borderwidth=0,
                                   command=self.answer_false)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_q()
            self.canvas.itemconfig(self.trivia_q, text=q_text)
            self.score.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.trivia_q, text="You've finished the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.answer_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.answer_feedback(is_right)

    def answer_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
