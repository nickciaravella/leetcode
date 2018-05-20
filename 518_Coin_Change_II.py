class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]

# For each coin, the solution is:
# Number of combinations only using smaller coins (dp[j])
# + 
# Number of combinations with using current coin (dp[j-coins[i]])
