# https://leetcode.com/problems/pascals-triangle-ii/description/
# Easy

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [0] * (rowIndex+1)
        dp[0] = 1
        for row in range(rowIndex+1):
            for column in range(row, 0, -1):
                dp[column] += dp[column-1]
            #print(dp)
        return dp

# Output for 5 with print statement
# [1, 0, 0, 0, 0, 0]
# [1, 1, 0, 0, 0, 0]
# [1, 2, 1, 0, 0, 0]
# [1, 3, 3, 1, 0, 0]
# [1, 4, 6, 4, 1, 0]
# [1, 5, 10, 10, 5, 1]