import random

def generate_secret_number(n):
    """Generate a random n-digit secret number."""
    return ''.join(random.choice('0123456789') for _ in range(n))

def get_guess(prompt, n):
    """Get a valid n-digit guess from the player."""
    while True:
        guess = input(prompt)
        if guess.isdigit() and len(guess) == n:
            return guess
        else:
            print(f"Invalid guess. Please enter a {n}-digit number.")

def evaluate_guess(secret, guess):
    """Evaluate the guess and return a hint."""
    hint = ''
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            hint += 'O'  # Digit is correct and in the right position
        elif guess[i] in secret:
            hint += 'X'  # Digit is correct but in the wrong position
        else:
            hint += '-'  # Digit is not in the secret number
    return hint

def play_mastermind(n):
    print("Let's play Mastermind!")
    print(f"Player 1 will set a {n}-digit secret number, and Player 2 will guess.")
    
    # Player 1 sets the secret number
    secret_number = generate_secret_number(n)
    attempts_p2 = 0
    
    while True:
        attempts_p2 += 1
        guess_p2 = get_guess(f"Player 2, enter your {n}-digit guess: ", n)
        
        if guess_p2 == secret_number:
            print(f"Congratulations, Player 2! You guessed the number {secret_number} correctly in {attempts_p2} attempts.")
            break
        
        hint = evaluate_guess(secret_number, guess_p2)
        print(f"Hint: {hint}")
    
    print("\nNow, Player 2 will set the secret number, and Player 1 will guess.")
    
    # Player 2 sets the secret number
    secret_number = generate_secret_number(n)
    attempts_p1 = 0
    
    while True:
        attempts_p1 += 1
        guess_p1 = get_guess(f"Player 1, enter your {n}-digit guess: ", n)
        
        if guess_p1 == secret_number:
            print(f"Congratulations, Player 1! You guessed the number {secret_number} correctly in {attempts_p1} attempts.")
            break
        
        hint = evaluate_guess(secret_number, guess_p1)
        print(f"Hint: {hint}")
    
    # Determine the winner
    if attempts_p1 < attempts_p2:
        print("\nPlayer 1 is crowned Mastermind! Guessed the number in fewer attempts.")
    elif attempts_p1 > attempts_p2:
        print("\nPlayer 2 is crowned Mastermind! Guessed the number in fewer attempts.")
    else:
        print("\nIt's a tie! Both players guessed the number in the same number of attempts.")

if __name__ == "__main__":
    n = 4  # You can change the number of digits for the secret number if desired
    play_mastermind(n)
