# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Easy

class Solution:
    # Don't overthink.. buy any day where you will have profit tomorrow
    # Sell tomorrow, there is no transaction fee ;)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(price-previous for previous, price in zip(prices[:-1], prices[1:]) if price > previous)