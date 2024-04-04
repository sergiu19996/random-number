from simple_term_menu import TerminalMenu
from main_game import *

# Variable to control returning to the main menu
back_to_main_menu = False

# Text of the game rules
rules_text = """
RULES:

1. Goal: The goal of the game is to guess the correct number within a certain range of values. Choose an integer number within this range and try to guess the correct number.
2. Range of Values: The game will have a defined range of values, for example, from 1 to 100. The player must guess the number within this range.
3. Guess Feedback: After each guess by the player, the game will provide feedback to indicate whether the guessed number is too high, too low, or correct. Based on this feedback, the player can adjust their next guess to get closer to the correct number.
"""

def main_menu():
    """
    Function to display the main menu and handle user options.
    """
    global back_to_main_menu
    
    options = ["Learn the rules", "Play the game", "Exit"]
    terminal_menu = TerminalMenu(options)
    
    while True:
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Learn the rules":
            print(rules_text)
            input("Press Enter to go back to the main menu...")
        elif options[menu_entry_index] == "Play the game":
            print("GAME")
            guess()
        elif options[menu_entry_index] == "Exit":
            print("EXIT")
            exit()
        
        if back_to_main_menu:
            back_to_main_menu = False
            break


def main():
    """
    Main function to run the game.
    """
    print(f"""
Welcome to the Guess Number Game!
You will need to ....

Let's start
    """)
    main_menu()


if __name__ == "__main__":
    main()

