import random

def select():
    while True:
        user_choice = input("Enter your choice Rock, Paper, or Scissors: ").lower()
        if user_choice in ("rock", "paper", "scissors"):
            return user_choice
        else:
            print("Invalid selection. Please choose rock, paper, or scissors.")

def computer_selection():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = select()
        computer_choice = computer_selection()
        
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")
        
        result = winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors game!")
    main() 
