# https://leetcode.com/problems/n-queens-ii/description/
# Hard

class Solution:
    
    def totalNQueens(self, n):
        self.n = n
        self.colIndex = [-1] * n
        return self.backtrack(0, 0)

    def backtrack(self, row, queens):        
        if queens == self.n:            
            return 1
        
        count = 0
        for column in range(self.n):
            if self.canPutQueen(row, column):
                self.colIndex[row] = column
                count += self.backtrack(row+1, queens+1)
                self.colIndex[row] = -1
        return count

    def canPutQueen(self, inrow, incolumn):
        for row in range(self.n):
            if self.colIndex[row] == -1:
                continue

            column = self.colIndex[row]
            if abs(incolumn-column) == abs(inrow-row) or column == incolumn:
                return False

        return True