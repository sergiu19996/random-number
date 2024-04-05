import random
import PySimpleGUI as sg

def guess():
    """
    Implements the guessing game logic.
    
    Randomly selects a number between 1 and 20, and prompts the user to guess it. 
    Provides feedback to the user whether the guessed number is too low or too high.
    Once the user guesses the correct number, congratulates the user.
    """
    random_number = random.randint(1, 20)
    guess = 0
    layout = [[sg.Text("Please enter a number between 1 and 20:")],
              [sg.InputText()],
              [sg.Button("Guess"), sg.Button("Exit")]]
    window = sg.Window("Guess Number Game", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        if event == "Guess":
            guess = int(values[0])
            if guess < random_number:
                sg.popup('Sorry, wrong number. Too low')
            elif guess > random_number:
                sg.popup('Sorry, guess again. Too high.')
            else:
                sg.popup('Congratulations! You guessed the number correctly!')
                break
    window.close()

def main_menu():
    """
    Function to display the main menu and handle user options.
    """
    layout = [[sg.Text("Welcome to the Guess Number Game!")],
              [sg.Text("You will need to ....")],
              [sg.Button("Learn the rules")],
              [sg.Button("Play the game")],
              [sg.Button("Exit")]]
    window = sg.Window("Main Menu", layout)
    
    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        if event == "Learn the rules":
            sg.popup(rules_text)
        elif event == "Play the game":
            guess()
    
    window.close()

if __name__ == "__main__":
    main_menu()