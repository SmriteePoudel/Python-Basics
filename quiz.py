class Quiz:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.score = 0

    def start_quiz(self):
        for question, answer in self.quiz_data.items():
            user_answer = input(question + " ")

            if user_answer.lower() == answer.lower():
                print("Correct Answer!")
                self.score += 1
            else:
                print("Wrong Answer!")

    def display_score(self):
        print("Final Score:", self.score)


quiz_data = {
    "Capital of Nepal?": "Kathmandu",
    "2 + 2 = ?": "4",
    "Color of sky?": "Blue"
}

quiz = Quiz(quiz_data)

quiz.start_quiz()
quiz.display_score()