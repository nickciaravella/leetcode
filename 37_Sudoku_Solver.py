# https://leetcode.com/problems/sudoku-solver/description/
# Hard

from collections import defaultdict

class Solution:

    def __init__(self):
        self.placesToFill = []
        self.columns = defaultdict(set)
        self.rows = defaultdict(set)
        self.squares = defaultdict(set)
        self.validNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def solveSudoku(self, board):  
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val == '.':
                    self.placesToFill.append((i,j))
                else:
                    self.rows[i].add(val)
                    self.columns[j].add(val)
                    self.squares[(i-i%3, j-j%3)].add(val)
        
        self.backtrack(board, 0)

    def backtrack(self, board, index):
        if index == len(self.placesToFill):
            return True

        i, j = self.placesToFill[index]
        for number in self.validNumbers:
            
            if not (number in self.rows[i] or number in self.columns[j] or number in self.squares[(i-i%3, j-j%3)]):
                board[i][j] = number
                self.rows[i].add(number)
                self.columns[j].add(number)
                self.squares[(i-i%3, j-j%3)].add(number)

                if self.backtrack(board, index+1):
                    return True
                else:                
                    board[i][j] = "."
                    self.rows[i].remove(number)
                    self.columns[j].remove(number)
                    self.squares[(i-i%3, j-j%3)].remove(number)

        return False

board = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]
board = [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]           
s = Solution()
s.solveSudoku(board)
for row in board:
    print(row)
