# https://leetcode.com/problems/minimum-path-sum/description/
# Medium

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        # Fill the first row with always going right        
        dp = [grid[0][0]]
        for j in range(1, len(grid[0])):
            dp.append(dp[j-1]+grid[0][j])
            
        for i in range(1, len(grid)):
            # There is no left for 0, so choose up
            dp[0] += grid[i][0]
            for j in range(1, len(grid[i])):
                # Choose the min of coming from up or coming from the left
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[-1]