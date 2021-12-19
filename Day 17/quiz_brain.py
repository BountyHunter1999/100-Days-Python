class QuizBrain:
    def __init__(self, questions_list):
        # any time a quiz object is created it starts with 0 
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        
    def next_question(self):
        current_question = self.questions_list[self.question_number].text
        user_answer = input(f"Q.{self.question_number+1} {current_question} (True/False)?: ")
        self.check_answer(user_answer)
        print(f"The user has {self.score} / {self.question_number + 1} points", end="\n")
        self.question_number += 1
        # return self.questions_list[self.question_number]

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_ans):
        correct_answer = self.questions_list[self.question_number].answer
        if user_ans[0].lower() == correct_answer[0].lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")

    # def __str__(self):
    #     return f"The user is at Q.N {self.question_number + 1} with {self.score} points"

