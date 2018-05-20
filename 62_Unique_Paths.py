# https://leetcode.com/problems/unique-paths/description/
# Medium

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
    
        return dp[-1]

# start with a 1x1, 1 unique path
# all paths 1xN or Nx1 also have 1 unique path
# for each cell, you can get to it by all the unique 
# ways to get to the square above or the square to the left
# This results in a formula (using matrix) of:
#   dp[i][j] = dp[i-1][j] + dp[i][j-1]
# The above algorithm is an optimization which saves space.