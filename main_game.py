import random


def guess():
    """
    Implements the guessing game logic.
    
    Randomly selects a number between 1 and 20, and prompts the user to guess it. 
    Provides feedback to the user whether the guessed number is too low or too high.
    Once the user guesses the correct number, congratulates the user.
    """
    random_number = random.randint(1, 20)
    guess = 0
    while guess != random_number:
        guess = read_number()
        if guess < random_number:
            print('Sorry, wrong number. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print('Congratulations! You guessed the number correctly!')


def read_number():
    """
    Reads an integer number from the user.

    Returns:
    int: The integer number entered by the user.
    """
    while True:
        number = input("Please enter a number between 1 and 20: ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= 20:
                return number
            else:
                print("Please enter a number between 1 and 20.")
        else:
            print("Please enter only digits.")
