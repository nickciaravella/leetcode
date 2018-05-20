# https://leetcode.com/problems/happy-number/description/
# Easy

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        cur = n
        while True:
            if cur == 1:
                return True
            elif cur in seen:
                return False
            else:
                seen.add(cur)
                cur = self.sum_of_squared_digits(cur)
        
    def sum_of_squared_digits(self, n):
        new_n = 0
        while n > 0:
            new_n += (n%10)**2
            n //= 10
        return new_n
