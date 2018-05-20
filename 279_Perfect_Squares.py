# https://leetcode.com/problems/perfect-squares/description/
# Medium

from time import time

from math import sqrt
from itertools import takewhile

# Using DP (knapsack problem)
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i*i for i in range(1, int(sqrt(n)+1))]

        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(len(dp)):
            for square in takewhile(lambda x: x <= i, squares):
                dp[i] = min(dp[i-square]+1, dp[i])

        return dp[n]

# Using BFS - much faster
class Solution2:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i*i for i in range(1, int(sqrt(n)+1))]
        queue = [(0,0)]
        seen = set()

        while queue:
            val, depth = queue.pop()

            for square in squares:                
                candidate = val+square
                
                if candidate == n:
                    return depth+1

                if candidate not in seen and candidate < n:
                    queue.insert(0, (candidate, depth+1))
                    seen.add(candidate)
        
        return -1

# print("Solution 1 (Knapsack)")
# s = Solution()
# t1 = time()
# print(s.numSquares(6730))
# t2 = time()
# print(t2-t1)

# print()
# print("Solution 2 (BFS)")
# s = Solution2()
# t1 = time()
# print(s.numSquares(6730))
# t2 = time()
# print(t2-t1)

# Solution 1 (Knapsack)
# 2
# 0.14758682250976562

# Solution 2 (BFS)
# 2
# 0.0007522106170654297