# https://leetcode.com/problems/n-queens/description/
# Hard

class Solution:
    
    def __init__(self):
        self.n = 0
        self.board = []
        self.queens = []
    
    def solveNQueens(self, n):
        self.n = n

        for i in range(n):
            self.board.append(list('.'*n))

        result = []
        self.backtrack(0, 0, result)
        return result

    def backtrack(self, i, j, result):
        if len(self.queens) == self.n:
            result.append([''.join(row) for row in self.board])
            return
        
        for i in range(i, self.n):
            for j in range(j, self.n):
                if self.canPutQueen(i, j):
                    self.board[i][j] = 'Q'
                    self.queens.append((i,j))
                    self.backtrack(i+1, 0, result)
                    self.queens.pop()
                    self.board[i][j] = '.'

    def canPutQueen(self, i, j):
        for queen in self.queens:
            if queen[1] == j or abs(j-queen[1]) == abs(i-queen[0]):
                return False
        return True
