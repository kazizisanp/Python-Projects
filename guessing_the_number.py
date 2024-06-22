import random

def number_guessing_game():
    
    # setting the range for the random number
    min_number = 1
    max_number = 100
    
    # generate a random number
    random_number = random.randint(min_number, max_number)
    
    # initialize the number of guesses user name
    guesses = 0
    print(f"Welcome to the Number Guessing Game!")
    print(f"Guess a number between {min_number} and {max_number}.")
    
    while True:
        try:
        # prompt the user to make a guess
            guess = int(input("Enter your guess: "))
            guesses += 1
        
        # check if the guess in correct 
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {guesses} tries.")
                break
    
        except ValueError:
            print("Invalid Input! Please enter a valid number.")
    
    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print("Thank you for playing! Goodbye.")

# start the game
number_guessing_game()