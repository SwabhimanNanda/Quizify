# Importing necessary classes and modules
from question_model import Question  # Importing the Question class from question_model.py
from data import question_data  # Importing the question data from data.py
from quiz_begin import QuizBrain  # Importing the QuizBrain class from quiz_begin.py
import random  # Importing the random module for shuffling the questions

# Creating an empty list to hold the questions
question_bank = []

# Shuffling the question data to randomize the order of questions
random.shuffle(question_data)

# Iterating over each question in the shuffled question data
for question in question_data:
    # Extracting the question text and answer from the current question dictionary
    question_text = question["text"]
    question_answer = question["answer"]
    # Creating a new Question object with the extracted text and answer
    new_question = Question(question_text, question_answer)
    # Adding the new Question object to the question bank list
    question_bank.append(new_question)

# Creating a QuizBrain object with the question bank list
quiz = QuizBrain(question_bank)

# Looping until there are no more questions in the quiz
while quiz.still_has_question():
    # Displaying the next question and getting user input for the answer
    quiz.next_question()

# Displaying a message indicating the end of the quiz and the final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
