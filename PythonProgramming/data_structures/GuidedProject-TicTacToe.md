### **Guided Project: Tic-Tac-Toe Game in Python**

#### **Objective:**
Create a two-player Tic-Tac-Toe game in Python, where players alternate turns to place their marks (X or O) on a 3x3 grid. The program should handle player input, display the board, check for a winner, and ensure that invalid moves are not allowed.

---

#### **Task Requirements:**

##### **1. Game Board:**
- Use a 3x3 grid to represent the board.
- Each cell on the board can either be empty (represented as `' '`), marked with `'X'`, or marked with `'O'`.
- The game will continue until one player wins or all cells are filled (draw).

##### **2. Players and Turns:**
- There are two players: Player X and Player O.
- Players take turns to enter their move, specifying the row and column where they want to place their mark.
- After each valid move, the game will display the updated board.

##### **3. Winning Conditions:**
- A player wins if they have three of their marks in a row, either:
  - Horizontally
  - Vertically
  - Diagonally (both diagonal directions)
- The game should check for a winner after each move.

##### **4. Draw Condition:**
- The game ends in a draw if all cells on the board are filled and no player has won.
- If the board is full and no winner is found, the game should display "It's a draw."

##### **5. Input Validation:**
- Players should be prompted to enter valid moves:
  - The row and column values should be integers between 0 and 2.
  - The selected cell must be empty. If the cell is already taken, the player should be prompted to try again.

##### **6. Displaying the Board:**
- The board should be displayed after each move, showing the current state of the game.

##### **7. Game Loop:**
- The game should continue alternating between players until either one wins or the board is full.
- The current player's turn should be displayed before their move.
- After each move, check if there is a winner or if the game ends in a draw.

##### **8. Error Handling:**
- If a player enters an invalid row or column, or if they choose a cell that is already occupied, display an appropriate message and ask for input again.
- Handle any unexpected input (e.g., non-numeric values) by prompting the player to enter valid input.

##### **9. Functionality:**
The program should be divided into the following functions:
- **`initialize_board()`**: Initializes the game board with empty cells.
- **`display_board(board)`**: Displays the current state of the board.
- **`is_valid_move(board, row, col)`**: Checks if the move is valid (the cell is within bounds and empty).
- **`check_win(board, player)`**: Checks if the given player has won the game.
- **`is_board_full(board)`**: Checks if the board is full.
- **`play_turn(board, player)`**: Handles player input for their move and updates the board.

