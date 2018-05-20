# https://leetcode.com/problems/coin-change/description/
# Medium

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """        
        dp = [0] + ([amount+1] * amount) # Neat trick to avoid using -1 which messes up min()
        for coin in coins:
            for i in range(coin,amount+1):            
                dp[i] = min(dp[i-coin]+1, dp[i])                    
        return dp[-1] if dp[-1] <= amount else -1

# Hard to understand from the algorithm, but it is just an optimization of a
# classic DP problem with the following grid and formula.

#  Coins = 1,2,5 Amount = 7
#     0   1   2   3   4   5   6   7
# 1   0   1   2   3   4   5   6   7
# 2   0   1   1   2   2   3   3   4
# 5   0   1   1   2   2   1   2   2  <-- Answer
# dp[i][j] = min(dp[i-coinValue]+1, dp[i-1][j])

# Since this formula on really needs the current and previous
# rows, we can store just one array instead of the full grid.