
### **Guided Project: Tic-Tac-Toe Game**

#### **Objective:**
Your goal is to create a two-player Tic-Tac-Toe game in C, where players alternate turns to place their marks (X or O) on a 3x3 grid. The program should check for a winner, display the board, and handle invalid moves.

#### **Task Requirements:**

##### **1. File Organization:**
The code should be split into three files:

1.  **main.h** — Contains function prototypes and necessary constants.
2. **tic_tac_toe.c** — Contains the game logic, such as checking for a win and handling player turns.
3. **main.c** — Contains the main game loop and user interaction.

##### **2. Core Logic Overview:**

- **Game Board:**  
  Use a 3x3 grid to represent the board. Each cell can be empty (a space), marked with 'X' or 'O'.
  
- **Switch Turns:**  
  Players X and O alternate taking turns. The current player should be displayed, and the next player should be selected after each valid move.
  
- **Winning Condition:**  
  The game ends when a player gets three marks in a row (horizontally, vertically, or diagonally).
  
- **Draw Condition:**  
  The game ends in a draw if the board is full and no player has won.
  
- **Input Validation:**  
  Players must provide valid moves (row and column within bounds, and not choosing a cell that is already taken).

##### **3. Specific Requirements for Files:**

#### **main.h** (Header File)

This file contains function prototypes and necessary constants.  
You should define the following functions:

- **`initializeBoard(char board[3][3])`**  
  Initializes the board by setting all cells to `' '` (empty).

- **`displayBoard(char board[3][3])`**  
  Displays the current state of the board in a user-friendly format.

- **`isValidMove(char board[3][3], int row, int col)`**  
  Returns 1 (true) if the move is valid (the cell is empty and within bounds), otherwise returns 0 (false).

- **`checkWin(char board[3][3], char player)`**  
  Checks if the specified player has won the game by having three of their marks in a row.

- **`isBoardFull(char board[3][3])`**  
  Checks if the board is full (no empty cells left). Returns 1 if full, 0 if not.

- **`playTurn(char board[3][3], char player)`**  
  Prompts the current player to enter their move (row and column). Validates the input and updates the board.

##### **main.c** (Main File)

This is where the main game loop runs. You will:

- **Initialize the game board** using `initializeBoard()`.
- **Display the board** using `displayBoard()`.
- **Handle player turns** using `playTurn()` and check for win or draw conditions after each turn.
- **Check for a winner** using `checkWin()` and print the result.
- **Check for a draw** using `isBoardFull()`.

Here’s the outline of the `main.c` file:

```c
#include <stdio.h>
#include "main.h"

int main() {
    char board[3][3];
    char currentPlayer = 'X';  // Start with player X

    initializeBoard(board);  // Initialize the game board

    while (1) {
        displayBoard(board);  // Show the current board
        playTurn(board, currentPlayer);  // Get the current player's move

        if (checkWin(board, currentPlayer)) {
            displayBoard(board);  // Show the final board
            printf("Player %c wins!\n", currentPlayer);
            break;
        }

        if (isBoardFull(board)) {
            displayBoard(board);  // Show the final board
            printf("It's a draw!\n");
            break;
        }

        // Switch to the next player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}
```

##### **4. Sample Output:**

Here’s an example of what the game might look like when it's running:

```
   |   |   
---|---|---
   |   |   
---|---|---
   |   |   

Player X, enter your move (row and column: 0-2): 0 0

X  |   |   
---|---|---
   |   |   
---|---|---
   |   |   

Player O, enter your move (row and column: 0-2): 1 1

X  |   |   
---|---|---
   | O |   
---|---|---
   |   |   

...
```

