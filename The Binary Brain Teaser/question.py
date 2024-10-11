import random

class Question:
    def __init__(self,max_question):
        self.question = ""
        self.Answer = ""
        self.question_number = 1
        self.AllQuestion = (len(max_question) + self.question_number)-1
        self.max_question = max_question
    
    def ChooseQuestion(self):
        self.question_number += 1
        CurrentQuestion = random.choice(self.max_question) 
        self.question = CurrentQuestion["question"]
        self.Answer = CurrentQuestion["correct_answer"]
        self.max_question.remove(CurrentQuestion)
        
    def AskQuestion(self):
        self.ChooseQuestion()
        return self.question
    def CheckAnswer(self,checking_type):
        if self.Answer.lower()==checking_type.lower():
            return True
        else:
            return False
        
    def CheckIfQuestionIsEnd(self):
        if len(self.max_question)>0:
            return True
        else :
            return False
    def answer(self):
        return self.Answer


    