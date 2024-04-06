"""
Connect Four
Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces which dropped in columns:

The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.
"""
import codewars_test as test
def who_is_winner(pieces_position_list):
    rows = 6
    cols = 7
    letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    grid = [['.' for j in range(cols)] for i in range(rows)]
    for pieces in pieces_position_list:
        pieces_arr = pieces.split('_')
        col = letter_to_number[pieces_arr[0]]
        color = pieces_arr[1][0]
        for row in range(rows):
            if grid[row][col]=='.':
                grid[row][col]=color
                is_winner = check_winner(grid, row, col,color)
                if is_winner:
                    if color =='Y':
                        return 'Yellow'
                    if color =='R':
                        return 'Red'
                break
    return 'Draw'

def check_winner(grid, row, col, color):
    #check horizontal
    if ''.join(grid[row]).__contains__(color*4):
        return color
    if ''.join([grid[r][col] for r in range(6)]).__contains__(color*4):
        return color
    row_up,row_down,col_up,col_down = row+1,row-1,col+1,col-1
    diagonal_right=[grid[row][col]]
    while row_up<len(grid) and col_up<(len(grid[0])):
        if grid[row_up][col_up] != '.':
            diagonal_right.append(grid[row_up][col_up])
            row_up+=1
            col_up+=1
        else:
            break
    while row_down>=0 and col_down>=0:
        if grid[row_down][col_down] != '.':
            diagonal_right.append(grid[row_down][col_down])
            row_down-= 1
            col_down-= 1
        else:
            break
    if ''.join(diagonal_right).__contains__(color * 4):
        return color
    row_up,row_down,col_up,col_down = row+1,row-1,col+1,col-1
    diagonal_left = [grid[row][col]]
    while row_up < len(grid) and col_down >=0:
        if grid[row_up][col_down] != '.':
            diagonal_left.append(grid[row_up][col_down])
            row_up += 1
            col_down -= 1
        else:
            break
    while row_down >= 0 and col_up <(len(grid[0])):
        if grid[row_down][col_up] != '.':
            diagonal_left.append(grid[row_down][col_up])
            row_down -= 1
            col_up += 1
        else:
            break
    if ''.join(diagonal_left).__contains__(color * 4):
        return color
    return None

@test.describe("Fixed tests")
def fixeds():
    test.assert_equals(who_is_winner([
        "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
        "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
        "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
    ]), "Yellow")

    test.assert_equals(who_is_winner([
        "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
        "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
        "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
        "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
        "E_Yellow", "E_Red"
    ]), "Yellow")

    test.assert_equals(who_is_winner([
        "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red",
        "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red",
        "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red",
        "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red",
        "B_Yellow", "B_Red"
    ]), "Red")

    test.assert_equals(who_is_winner([
        "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
        "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
    ]), "Red")

    test.assert_equals(who_is_winner([
        "A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
    ]), "Yellow")

    test.assert_equals(who_is_winner([
        "A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
    ]), "Draw");

