# Display the board nicely
def display_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end='')


# Find the blank space in Sudoku's board
def find_blank(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # return as row, col
    return None


# Solve the Sudoku using backtracking algorithm
def solver(bo):
    blank_position = find_blank(bo)
    if not blank_position:
        return True
    else:
        row, col = blank_position

    for i in range(1, 10):
        # Backtrack if i fully iterated and return False
        if check_valid(bo, i, (row, col)):
            bo[row][col] = i

            # Recursion occurs
            if solver(bo):
                return True

            # Remove (backtrack) and try next digit
            bo[row][col] = 0
    return False


# Check whether it satisfies the constraints of the problem
def check_valid(bo, num, pos):
    # Check row
    # pos[0] = i = row, pos[1] = j = col
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    # the current box of the position that lies
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loop through the current box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True
