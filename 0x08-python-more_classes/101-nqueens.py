#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
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
    board = [[0] * n for _ in range(n)]

    def solve_util(row):
        if row == n:
            print_solution(board)
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_util(row + 1)
                board[row][col] = 0

    def print_solution(board):
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
