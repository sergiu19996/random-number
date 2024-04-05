from PyInquirer import prompt
from main_game import guess, rules_text

def main_menu():
    """
    Function to display the main menu and handle user options.
    """
    while True:
        options = [
            {"type": "list", "name": "menu_choice", "message": "Main Menu", "choices": [
                "Learn the rules",
                "Play the game",
                "Exit"
            ]}
        ]
        menu_choice = prompt(options)["menu_choice"]

        if menu_choice == "Learn the rules":
            print(rules_text)
            input("Press Enter to go back to the main menu...")
        elif menu_choice == "Play the game":
            print("GAME")
            guess()
        elif menu_choice == "Exit":
            print("EXIT")
            exit()

if __name__ == "__main__":
    print("""
    Welcome to the Guess Number Game!
    You will need to ....

    Let's start
    """)
    main_menu()