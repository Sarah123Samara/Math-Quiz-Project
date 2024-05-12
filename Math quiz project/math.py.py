import random
import time


def generate_question(level):
    def generate_integer_question(level, min_num, max_num):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        operator = random.choice(["+", "-", "*", "/"])
        if operator == "/" and num1 % num2 != 0:
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, max_num)
            while num1 % num2 != 0:
                num1 = random.randint(min_num, max_num)
                num2 = random.randint(min_num, max_num)
        question = f"{num1} {operator} {num2}"
        answer = eval(question)
        return question, int(answer)

    if level == "Easy":
        question, answer = generate_integer_question(level, 1, 10)
    elif level == "Medium":
        question, answer = generate_integer_question(level, 1, 50)
    elif level == "Hard":
        question, answer = generate_integer_question(level, 1, 100)

    while level == "Easy" and (answer < 1 or answer > 10):
        question, answer = generate_integer_question(level, 1, 10)
    while level == "Medium" and (answer < 1 or answer > 50):
        question, answer = generate_integer_question(level, 1, 50)
    while level == "Hard" and (answer < 1 or answer > 100):
        question, answer = generate_integer_question(level, 1, 100)

    return question, answer


def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a valid number (integer).")


def game():
    while True:
        print("Welcome to Quick Math")
        print("Choose the level you want to play:")
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")
        choice = get_integer_input("Enter the number of your choice: ")

        if choice == 1:
            level = "Easy"
            break
        elif choice == 2:
            level = "Medium"
            break
        elif choice == 3:
            level = "Hard"
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    num_questions = 10
    incorrect_answers = []
    start_time = time.time()

    for i in range(1, num_questions + 1):
        question, correct_answer = generate_question(level)
        while True:
            if "x" in question:  # Replace 'x' with the multiplication sign
                question = question.replace("x", "×")
            print(f"Q{i}: {question}  =", end=" ")
            user_answer = input()

            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number (integer).")

        if user_answer != correct_answer:
            incorrect_answers.append((f"Q{i}: {question}", correct_answer))

    end_time = time.time()
    total_time = end_time - start_time

    print(
        f"You got {num_questions - len(incorrect_answers)} out of {num_questions} questions correct"
    )
    print(f"It took you {total_time:.2f} seconds to complete")

    if incorrect_answers:
        print("Questions answered incorrectly:")
        for question, correct_answer in incorrect_answers:
            print(f"{question} = {correct_answer}")

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

    if play_again == "yes":
        game()
    else:
        print("Thank You for playing. Have a nice day.")


if __name__ == "__main__":
    game()
