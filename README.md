# Guess the Number

## Description
This project represents a simple game where the user tries to guess a randomly generated integer between 1 and 20.

## Usage
To use this project, follow the steps below:

1. **Main Menu:** At the start, the user will encounter a main menu offering the following options:
    - **Learn the Rules:** Displays the rules of the game.
    - **Play the Game:** Initiates the actual game.
    - **Exit:** Exits the application.

2. **Learn the Rules:**
    - Once the user selects this option, the rules of the game will be displayed, after which the user can return to the main menu.

3. **Play the Game:**
    - The game begins by generating a random number between 1 and 20.
    - The user will then be prompted to input an integer between 1 and 20 and try to guess the generated number.
    - If the user's guess is lower or higher than the generated number, they will receive a corresponding message and will be asked to guess again.
    - The game continues until the user correctly guesses the generated number.
    - After the user correctly guesses the number, a congratulatory message will be displayed, and the user can return to the main menu.

4. **Exit:**
    - This option closes the application.

## Installation
To install and run this project locally, follow the steps below:

1. Clone this repository:
    ```bash
    git clone https://github.com/user/guess-the-number.git
    ```
2. Navigate into the project directory:
    ```bash
    cd guess-the-number
    ```
3. Install the dependencies using pip (Python Package Installer):
    ```bash
    pip install -r requirements.txt
    ```
4. Run the main script:
    ```bash
    python guess_the_number.py
    ```

## Functionality
- **Random Number Generation:** The game generates a random number between 1 and 20 for the user to guess.
- **User Input Validation:** The project validates user input to ensure it is a digit between 1 and 20.
- **Interactive Menu:** The main menu and navigation between different options are handled through an interactive terminal menu.
- **Game Loop:** The game runs in a loop until the user chooses to exit or correctly guesses the generated number.

## System Requirements
This project requires Python 3 and the following Python libraries installed:
- `random`
- `simple_term_menu`



