# Question 8: Solve the N-Queens problem using backtracking.


def is_safe(board, row, column, size):
    # Check the same column in earlier rows.
    for previous_row in range(row):
        if board[previous_row] == column:
            return False

        # Check both diagonals.
        if abs(board[previous_row] - column) == abs(previous_row - row):
            return False

    return True


def solve_queens(board, row, size):
    if row == size:
        return True

    for column in range(size):
        if is_safe(board, row, column, size):
            board[row] = column

            if solve_queens(board, row + 1, size):
                return True

            # Backtrack if this position does not lead to a solution.
            board[row] = -1

    return False


size = int(input("Enter board size (try 4 or 8): "))

if size < 1:
    print("Board size must be positive.")
else:
    board = [-1] * size

    if solve_queens(board, 0, size):
        print("One valid solution:")
        for row in range(size):
            line = ""
            for column in range(size):
                if board[row] == column:
                    line = line + "Q "
                else:
                    line = line + ". "
            print(line)
    else:
        print("No solution exists for this board size.")
