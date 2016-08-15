'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''
class Solution(object):
    def isValidSudoku(self, board):
        if not board:
            return True

        for row in xrange(9):
            usedCol = []
            usedRow = []
            usedSqr = []
            for col in xrange(9):
                usedCol.append(False)
                usedRow.append(False)
                usedSqr.append(False)
            for col in xrange(9):
                valRow = board[row][col]
                if valRow != ".":
                    if usedRow[int(valRow) - 1]:
                        return False
                    usedRow[int(valRow) - 1] = True

                valCol = board[col][row]
                if valCol != ".":
                    if usedCol[int(valCol) - 1]:
                        return False
                    usedCol[int(valCol) - 1] = True
                rowSquare = int(row / 3) * 3 + (col / 3);
                colSquare = (row % 3) * 3 + col % 3;
                valSquare = board[rowSquare][colSquare]
                if valSquare != ".":
                    if usedSqr[int(valSquare) - 1]:
                        return False
                    usedSqr[int(valSquare) - 1] = True
        return True

if __name__ == "__main__":
    s = Solution()
    assert True == s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
    assert False == s.isValidSudoku(["787654321","2........","3........","4........","5........","6........","7........","8........","9........"])