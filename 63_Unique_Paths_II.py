# https://leetcode.com/problems/unique-paths-ii/description/
# Medium

# Same solution as 62_Unique_Paths, but if we hit and obstacle, reset
# that cell back to 0 (no way to get there).
# Hardest part is reducing the code down by analyzing the if conditions.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:                
                    dp[j] += dp[j-1]      
        return dp[-1]