# https://leetcode.com/problems/number-of-islands/description/
# Medium

class Solution:
    
    # O(n) where n == number of cells in matrix
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.floodFill(grid, i, j)
                    islands += 1
        return islands
    
    def floodFill(self, grid, i, j):
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        for movei, movej in moves:
            newi, newj = movei+i, movej+j
            if newi < 0 or newj < 0 or newi >= len(grid) or newj >= len(grid[i]) or grid[newi][newj] != '1':
                continue            
            grid[newi][newj] = '2'
            self.floodFill(grid, newi, newj)            