#include <stdio.h>
#include "tic_tac_toe.h"

// Function to initialize the board with empty spaces
void initializeBoard(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}

// Function to display the board
void displayBoard(char board[3][3]) {
    printf("\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf(" %c ", board[i][j]);
            if (j < 2) printf("|");
        }
        printf("\n");
        if (i < 2) printf("---|---|---\n");
    }
    printf("\n");
}

// Function to check if a move is valid
int isValidMove(char board[3][3], int row, int col) {
    return row >= 0 && row < 3 
           && col >= 0 && col < 3 && board[row][col] == ' ';
}

// Function to check if a player has won
int checkWin(char board[3][3], char player) {
    // Check rows, columns, and diagonals
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return 1;
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return 1;
    }
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return 1;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return 1;
    return 0;
}

// Function to check if the board is full (no empty spaces)
int isBoardFull(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') return 0;
        }
    }
    return 1;
}

// Function to play a single turn
void playTurn(char board[3][3], char player) {
    int row, col;
    printf("Player %c, enter your move (row and column: 0-2): ", player);
    scanf("%d %d", &row, &col);

    while (!isValidMove(board, row, col)) {
        printf("Invalid move. Try again (row and column: 0-2): ");
        scanf("%d %d", &row, &col);
    }

    board[row][col] = player;
}
