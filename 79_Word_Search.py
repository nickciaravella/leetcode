# https://leetcode.com/problems/word-search/description/
# Medium

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    board[i][j] = None
                    if self.backtrack(board, word[1:], i, j):
                        return True
                    board[i][j] = word[0]
        return False
                    
    def backtrack(self, board, word, i, j):
        if not word:
            return True
        
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        for movei, movej in moves:
            newi, newj = i+movei, j+movej
            if newi >= 0 and newi < len(board) and newj >= 0 and newj < len(board[newi]) and board[newi][newj] == word[0]:
                board[newi][newj] = None
                if self.backtrack(board, word[1:], newi, newj):
                    return True
                else:
                    board[newi][newj] = word[0]
                    
        return False