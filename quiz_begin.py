class QuizBrain:
    def __init__(self, q_list):
        """
        Initializes the QuizBrain object with the provided list of questions.

        Parameters:
        - q_list (list): List of Question objects.
        """
        self.question_number = 0  # Initialize question number to track progress
        self.score = 0  # Initialize score to track correct answers
        self.question_list = q_list  # Store the list of questions

    def still_has_question(self):
        """
        Checks if there are still questions remaining in the quiz.

        Returns:
        - bool: True if there are remaining questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Displays the next question and gets user input for the answer.
        """
        # Get the current question from the question list
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # Increment question number for next question

        # Get user input for the answer
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')

        # Check the user's answer against the correct answer
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks the user's answer against the correct answer and updates the score.

        Parameters:
        - user_answer (str): The user's answer ('True' or 'False').
        - correct_answer (str): The correct answer ('True' or 'False').
        """
        # Convert both answers to lowercase for case-insensitive comparison
        user_answer = user_answer.lower()
        correct_answer = correct_answer.lower()

        # Check if the user's answer matches the correct answer
        if user_answer == correct_answer:
            print('Correct!')
            self.score += 1  # Increment score for correct answer
        else:
            print('Incorrect!')
            # Provide the correct answer to the user
            print(f"The correct answer is: {correct_answer}")

        # Display the current score and question number
        print(f"The score is: {self.score}/{self.question_number}\n")


