# https://leetcode.com/problems/reverse-integer/description/
# Easy

class Solution(object):
    
    MIN = -1 * (2**31)
    MAX = (2**31)-1
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        if x < 0:
            reverse = int('-' + str(x)[1:][::-1])
        else:
            reverse = int(str(x)[::-1])
            
        if reverse > self.MAX or reverse < self.MIN:
            return 0
            
        return reverse