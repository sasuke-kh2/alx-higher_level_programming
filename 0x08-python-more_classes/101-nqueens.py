#!/usr/bin/python3
"""
N-Queens Solver

This module provides a solution for the N-Queens problem,
which is the challenge of placing N non-attacking queens on an N×N chessboard.

Usage:
    python nqueens.py N

Where:
    - N (int): The size of the chessboard and the number of
    queens to be placed.
              Must be an integer greater than or equal to 4.

If the user provides the wrong number of arguments or invalid input,
the program will print an error message and exit with status 1.

Examples:
    $ python nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

    $ python nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]

"""
import sys


def is_safe(board, row, col, n):
    """
    Check if placing a queen at position (row, col) on the board is safe.

    Parameters:
    - board (list): The current state of the chessboard.
    - row (int): The row index where the queen is to be placed.
    - col (int): The column index where the queen is to be placed.
    - n (int): The size of the chessboard.

    Returns:
    - bool: True if it is safe to place a queen at the given position,
            False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(n):
    """
    Solve the N-queens problem and print all possible solutions.

    Parameters:
    - n (int): The size of the chessboard.
    """
    board = [[0] * n for _ in range(n)]

    def solve_util(row):
        """
        A recursive helper function to solve the N-queens problem.

        Parameters:
        - row (int): The current row being considered.

        Returns:
        - bool: True if a solution is found, False otherwise.
        """
        if row == n:
            print_solution(board)
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_util(row + 1)
                board[row][col] = 0

    def print_solution(board):
        """
        Print the current solution represented by the board.

        Parameters:
        - board (list): The current state of the chessboard.
        """
        queens = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    queens.append([i, j])
        print(queens)

    solve_util(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
