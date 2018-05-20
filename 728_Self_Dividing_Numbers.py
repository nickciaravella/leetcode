# https://leetcode.com/problems/self-dividing-numbers/description/
# Easy

class Solution(object):
    
    def isSelfDividing(self, num):
        temp = num
        while temp:
            digit = temp % 10
            if digit == 0 or num % digit != 0:
                return False
            temp /= 10
        return True
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return filter(self.isSelfDividing, range(left, right+1))