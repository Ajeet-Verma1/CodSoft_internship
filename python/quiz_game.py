import random

# Quiz Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "London", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    }
]

def get_random_question():
    return random.choice(questions)

def get_user_answer(question):
    print(question["question"])

    if "options" in question:
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
    else:
        print("Type your answer:")

    return input().strip()

def check_answer(question, user_answer):
    return user_answer.lower() == question["answer"].lower()

def display_result(score, total_questions):
    print(f"Your score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100

    if percentage == 100:
        print("Perfect! You got all the answers correct!")
    elif percentage >= 70:
        print("Well done! You did a great job!")
    else:
        print("Keep practicing! You can do better next time.")

def play_quiz():
    print("Welcome to the Quiz Game!")
    print("You will be presented with multiple-choice and fill-in-the-blank questions.")

    total_questions = len(questions)
    score = 0

    while True:
        question = get_random_question()
        user_answer = get_user_answer(question)

        if check_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")

        total_questions -= 1

        if total_questions == 0:
            break

        play_again = input("Do you want to continue? (yes/no): ").lower()
        if play_again != 'yes':
            break

    display_result(score, len(questions))

if __name__ == "__main__":
    play_quiz()

