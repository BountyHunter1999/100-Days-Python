from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=290,
                                                     # text="Question here",
                                                     fill=THEME_COLOR,
                                                     font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_bt = Button(image=true_img,
                              highlightthickness=0,
                              command=self.true_ans)
        self.true_bt.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_bt = Button(image=false_img,
                               highlightthickness=0,
                               command=self.cross_ans
                               )
        self.false_bt.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def show_score(self):
        score = self.quiz_brain.score
        self.score_label.config(text=f"Score: {score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.show_score()
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the Quiz Reached")
            self.true_bt.config(state="disabled")
            self.false_bt.config(state="disabled")

    def show_ans_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
            # self.canvas.config(bg="white")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def true_ans(self):
        ans = self.quiz_brain.check_answer("True")
        self.show_ans_feedback(ans)

    def cross_ans(self):
        ans = self.quiz_brain.check_answer("False")
        self.show_ans_feedback(ans)
