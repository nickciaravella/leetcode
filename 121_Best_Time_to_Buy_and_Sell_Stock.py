# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Easy

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price = 0
        current_best = 0
        for price in prices[::-1]:            
            max_price = max(price, max_price)
            current_best = max(current_best, max_price - price)
        return current_best
    