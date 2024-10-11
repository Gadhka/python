#from .question import Question
from data  import question_data
from question import Question
class StartApp(Question):
    def __init__(self,max_question):
        super().__init__(max_question)
        self.score = 0

    def App(self):
        
        while self.CheckIfQuestionIsEnd():
            guess =  input(f"Q:{self.question_number} {self.score}/{self.question_number-1} {self.AskQuestion()} (true,false)? ")
            if self.CheckAnswer(guess):
                self.score += 1
                print("You Got It")
            else:
                print("Thats Wrong ")
            print(F"The Correct Answer Was: {self.answer()}")
            print(f"Youre Current Score Is {self.score}/{self.question_number-1}")
        if  self.CheckIfQuestionIsEnd()==False :
            print("Game Is Over! ")
            print(f"Youre Current Score Is {self.score}/{self.AllQuestion} for {self.question_number-1}: Questions")
        


if __name__ == "__main__":
    Question_data = question_data
    StartApp(Question_data).App()