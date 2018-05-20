# https://leetcode.com/problems/max-area-of-island/description/
# Easy

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.find_area(grid, i, j))
        
        return max_area

    def find_area(self, grid, i, j):
        queue = [(i,j)]
        grid[i][j] = -1
        total = 0
        while queue:
            curi,curj = queue.pop()        
            total += 1

            next_moves = [(curi+movei,curj+movej) for movei, movej in [(1,0), (-1,0), (0,1), (0,-1)] 
                                            if (0 <= curi+movei < len(grid) and 
                                                0 <= curj+movej < len(grid[curi+movei]) and 
                                                grid[curi+movei][curj+movej] == 1)]

            for move in next_moves:
                grid[move[0]][move[1]] = -1
                queue.append((move[0], move[1]))                

        return total
                       

# s = Solution()
# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# print(s.maxAreaOfIsland(grid))