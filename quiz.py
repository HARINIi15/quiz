import random


questions = [
    {
        "question": "1. What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Rome"],
        "correct_answer": "B",
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B",
    },
    {
        "question": "3. What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Dolphin"],
        "correct_answer": "B",
    },
]


def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    return user_answer


def evaluate_answer(question, user_answer, score):
    if user_answer == question["correct_answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {question['correct_answer']}.\n")
    return score


def play_quiz():
    player_name = input("Enter your name: ")  
    print(f"Welcome to the Quiz Game, {player_name}!")
    print("You will be asked multiple-choice questions. Choose the correct option.")
    score = 0

    for question in questions:
        user_answer = display_question(question)
        score = evaluate_answer(question, user_answer, score)

    print(f"Your final score, {player_name}, is: {score}/{len(questions)}")


while True:
    play_quiz()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("Thank you for playing! Goodbye.")
