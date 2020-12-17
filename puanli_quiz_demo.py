# Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, question):
        self.questions = question
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("score: ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100, '*'))
    
q1 = Question('En iyi programlama dii hangisidir?', ['c#','python','javascript','java'], 'javascript')
q2 = Question('En popüler programlama dii hangisidir?', ['python', 'c#', 'javascript', 'java'], 'python')
q3 = Question('En çok kazandıran programlama dii hangisidir?', ['javascript', 'python', 'java', 'c#'], 'java')
q4 = Question('En çok sevilen programlama dii hangisidir?', ['javascript', 'python', 'java', 'c#'], 'c#')
q5 = Question('En kolay kazandıran programlama dii hangisidir?', ['javascript', 'python', 'java', 'c#'], 'python')
question = [q1,q2,q3,q4,q5]

quiz = Quiz(question)

quiz.loadQuestion()