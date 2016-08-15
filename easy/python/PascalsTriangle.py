'''
Given numRows, generate the first numRows of Pascal's triangle.
'''
class Solution(object):
    def generate(self, numRows):
        if numRows <= 0:
            return []
        sol = [[1], [1, 1]]
        if numRows == 1:
            return [sol[0]]
        if numRows == 2:
            return sol

        i = 2
        while i < numRows:
            newRow = [0] * (i - 1)
            j = 1
            while j < len(sol[i - 1]):
                newRow[j - 1] = sol[i - 1][j] + sol[i - 1][j - 1]
                j += 1
            newRow = [1] + newRow + [1]
            sol.append(newRow)
            i += 1
        return sol


if __name__ == "__main__":
    assert  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] == Solution().generate(5)