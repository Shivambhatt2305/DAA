grid = [[0] * 9 for _ in range(9)]

def is_safe(row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:

                for num in range(1, 10):
                    if is_safe(row, col, num):
                        grid[row][col] = num

                        if solve_sudoku():
                            return True

                        grid[row][col] = 0

                return False
    return True


# MAIN PROGRAM
print("Enter 9x9 Sudoku grid (use 0 for empty cells):")

for i in range(9):
    row = list(map(int, input().split()))
    grid[i] = row

if solve_sudoku():
    print("\nSolved Sudoku:")
    for i in range(9):
        print(*grid[i])
else:
    print("No solution exists")
