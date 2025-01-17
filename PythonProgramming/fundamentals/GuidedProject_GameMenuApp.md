# Game Menu Application

## Goal

This project introduces modular programming in Python using loops, conditions, and functions. The goal is to create a menu-driven application that allows users to select and play different games, each designed to practice basic programming concepts.

---

## Game Menu Structure

The program consists of two files:

1. **`main.py`:**
   - Provides a menu-driven interface for the user to select and play games.
   - Displays the options and takes user input to choose a game.
   - Calls functions from `games.py` to run the selected game.

2. **`games.py`:**
    - Each game (Guess the Number, Rock Paper Scissors, Math Quiz) should be implemented in its own function for clear organization and easy extensibility.
    - Functions should handle game logic, user input, and display relevant feedback after each round.
    - Make the functions modular, allowing each to be invoked independently.

   - **The games included are:**
     - **Guess the Number:**
       - Randomly select a number between 1 and 100 for the user to guess.
       - Provide hints like "Too Low" or "Too High" based on the user’s input.
       - Allow the user to keep guessing until they find the correct number, tracking the number of attempts.
     
     - **Rock, Paper, Scissors:**
       - Allow the user to select one of "Rock", "Paper", or "Scissors."
       - Randomly generate the computer's choice and determine the winner based on the classic rules (Rock beats Scissors, Scissors beats Paper, Paper beats Rock).
       - Display the result of each round (win, lose, or draw) and give the option to play again.

     - **Math Quiz:**
       - Generate random arithmetic questions (addition, subtraction, multiplication, division) with integer results.
       - Validate user answers and provide feedback (correct or incorrect) after each question.
       - Track the user's score or number of correct answers across multiple questions, allowing them to continue or exit after each round.

---

## Sample Menu

```
=== Game Menu ===
1. Guess the Number
2. Rock, Paper, Scissors
3. Math Quiz
0. Exit
Enter your choice: 
```

---



## Next Steps

After completing this project:

- Expand the application by adding new games or features.
- Implement advanced concepts like file handling or data structures.
- Explore creating graphical user interfaces (GUIs) for the application.

