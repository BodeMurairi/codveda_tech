#!/usr/bin/env python3

def print_board(board):
    print("\nSolution:\n")
    for row in board:
        for cell in row:
            print("Q" if cell == 1 else ".", end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    # Check same row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


def main():
    print("N-Queens Solver")
    print("=" * 25)

    try:
        n = int(input("Enter value of N (>= 4 recommended): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if n < 1:
        print("N must be positive.")
        return

    # Create NxN board initialized with 0
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print_board(board)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
