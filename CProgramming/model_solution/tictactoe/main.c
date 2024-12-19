#include <stdio.h>
#include "tic_tac_toe.h"

int main() {
    char board[3][3];
    char currentPlayer = 'X';

    initializeBoard(board);

    while (1) {
        displayBoard(board);
        playTurn(board, currentPlayer);

        if (checkWin(board, currentPlayer)) {
            displayBoard(board);
            printf("Player %c wins!\n", currentPlayer);
            break;
        }

        if (isBoardFull(board)) {
            displayBoard(board);
            printf("It's a draw!\n");
            break;
        }

        // Switch player
        if (currentPlayer == 'X')
            currentPlayer == 'O';
        else
            currentPlayer == 'X';

        // currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}
