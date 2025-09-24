ROWS = 6
COLS = 7

def create_grid():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_grid(grid):
    for row in grid:
        print("| " + " | ".join(row) + " |")
    print("  " + "   ".join(str(i) for i in range(COLS)))

def drop_piece(grid, col, piece):
    for row in reversed(grid):
        if row[col] == " ":
            row[col] = piece
            return True
    return False
