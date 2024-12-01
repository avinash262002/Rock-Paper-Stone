import random

def print_welcome_message():
    print("Welcome to the Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    print("You can type 'exit' anytime to end the game.\n")

def get_user_choice():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Your choice (1/2/3): ").strip()
    return choice

def convert_choice_to_string(choice):
    if choice == "1":
        return "Rock"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissors"
    return None

def get_computer_choice():
    return random.choice(["1", "2", "3"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "1" and computer_choice == "3") or \
         (user_choice == "2" and computer_choice == "1") or \
         (user_choice == "3" and computer_choice == "2"):
        return "User"
    else:
        return "Computer"

def display_round_result(user_choice_str, computer_choice_str, winner):
    print(f"\nYou chose: {user_choice_str}")
    print(f"Computer chose: {computer_choice_str}")
    if winner == "Draw":
        print("It's a draw!")
    elif winner == "User":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    print("\n" + "-" * 30)

def main():
    print_welcome_message()
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\nRound {round_number}")
        user_choice = get_user_choice()

        if user_choice.lower() == "exit":
            print("Exiting the game. Thanks for playing!")
            break

        user_choice_str = convert_choice_to_string(user_choice)
        if not user_choice_str:
            print("Invalid input! Please choose 1, 2, or 3.\n")
            continue

        computer_choice = get_computer_choice()
        computer_choice_str = convert_choice_to_string(computer_choice)

        winner = determine_winner(user_choice, computer_choice)

        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1

        display_round_result(user_choice_str, computer_choice_str, winner)

        print(f"Current Score - You: {user_score}, Computer: {computer_score}\n")
        round_number += 1

if __name__ == "__main__":
    main()
