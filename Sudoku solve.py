def print_board(board):
    """Function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    """Check if it's valid to place a number in the given row, column, and subgrid."""
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """Function to solve the Sudoku board using backtracking."""
    # Find an empty spot on the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing numbers 1-9 in the empty spot
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Recursively try to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # If placing num didn't lead to a solution, reset the spot and backtrack
                        board[row][col] = 0

                # If no number 1-9 leads to a solution, return False to backtrack
                return False

    # If there are no empty spots left, the board is solved
    return True

# Example Sudoku puzzle (0 represents empty spots)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku board:")
print_board(board)

if solve_sudoku(board):
    print("\nSudoku solved successfully!")
    print_board(board)
else:
    print("\nNo solution exists for the given Sudoku board.")
