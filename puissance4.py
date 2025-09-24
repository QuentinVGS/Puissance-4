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

def check_win(grid, piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(grid[r][c+i] == piece for i in range(4)):
                return True
    # Vertical
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(grid[r+i][c] == piece for i in range(4)):
                return True
    # Diagonal \
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(grid[r+i][c+i] == piece for i in range(4)):
                return True
    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(grid[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def play_game():
    grid = create_grid()
    game_over = False
    turn = 0

    while not game_over:
        print_grid(grid)
        col = int(input(f"Player {turn+1} ({'X' if turn==0 else 'O'}) - Choose column (0-{COLS-1}): "))

        if 0 <= col < COLS and drop_piece(grid, col, "X" if turn==0 else "O"):
            if check_win(grid, "X" if turn==0 else "O"):
                print_grid(grid)
                print(f"Player {turn+1} wins!")
                game_over = True
            turn = 1 - turn
        else:
            print("Invalid move, try again!")

play_game()
