from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank =[]

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    q1 = Question(question_text, question_answer)
    question_bank.append(q1)
    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()    

print(f"You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_no}")