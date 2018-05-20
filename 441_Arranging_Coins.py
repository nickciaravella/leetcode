# https://leetcode.com/problems/arranging-coins/description/
# Easy

# There is a math solution, since the stairs require n*(n+1) / 2 coins. 
# Below is an iterative solution.

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        count = 0
        while n >= i:
            count += 1
            n -= i
            i += 1
        return count