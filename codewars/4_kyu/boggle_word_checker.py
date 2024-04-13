"""
Write a function that determines whether a string is a valid guess in a Boggle board, as per the rules of Boggle.
A Boggle board is a 2D array of individual characters, e.g.:

[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]
Valid guesses are strings which can be formed by connecting adjacent cells (horizontally, vertically, or diagonally)
without re-using any previously used cells.

For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be valid guesses,
 while "BUNGIE", "BINS", and "SINUS" would not.

Your function should take two arguments (a 2D array and a string) and return true or false depending on
 whether the string is found in the array as per Boggle rules.

Test cases will provide various array and string sizes (squared arrays up to 150x150 and
strings up to 150 uppercase letters). You do not have to check whether the string is a real word or not,
 only if it's a valid guess.
"""
import codewars_test as test
import copy

def find_word(board, word):
    def dfs(row, col, index):
        # If we have traversed all characters in the word, return True
        if index == len(word):
            return True

        # Check if the current cell is out of bounds or doesn't match the current character in the word
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != word[index]:
            return False

        # Mark the current cell as visited by replacing its value with '#'
        grid[row][col] = '#'
        # Check adjacent cells
        is_found = any(dfs(row + u, col + v, index + 1)
                for u in [-1,0,1]
                for v in [-1,0,1])
        # Restore the original value of the cell
        grid[row][col] = word[index]

        return is_found
    grid = copy.deepcopy(board)
    return any(dfs(i,j,0)
            for i in range(len(grid))
            for j in range(len(grid[0])))



@test.describe("Sample tests")
def f1():
    testBoard = [
        ["E", "A", "R", "A"],
        ["N", "L", "E", "C"],
        ["I", "A", "I", "S"],
        ["B", "Y", "O", "R"]
    ]
    test.assert_equals(find_word(testBoard, "BAILER"), True, "Test for BAILER")
    test.assert_equals(find_word(testBoard, "EAR"), True, "Test for EAR")
    test.assert_equals(find_word(testBoard, "C"), True, "Test for C")
    test.assert_equals(find_word(testBoard, "EARS"), False, "Test for EARS")
    test.assert_equals(find_word(testBoard, "RSCAREIOYBAILNEA"), True, "Test for RSCAREIOYBAILNEA")
    test.assert_equals(find_word(testBoard, "CEREAL"), False, "Test for CEREAL")
    test.assert_equals(find_word(testBoard, "ROBES"), False, "Test for ROBES")