def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check same row on the left
        for c in range(col):
            if board[row][c] == 'Q':
                return False

        # Check upper-left diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Check lower-left diagonal
        r, c = row, col
        while r < n and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1

        return True

    def backtrack(col):
        if col >= n:
            current_solution = ["".join(row) for row in board]
            solutions.append(current_solution)
            return

        for row in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'

    backtrack(0)
    return solutions


def print_solutions(solutions):
    if not solutions:
        print("No solutions found.")
        return

    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row_str in solution:
            print(row_str)
        print()


n = 4
found_solutions = solve_n_queens(n)
print_solutions(found_solutions)
