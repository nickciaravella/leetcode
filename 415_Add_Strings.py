# https://leetcode.com/problems/add-strings/description/
# Easy

from itertools import zip_longest

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """        
        val = ''
        carry = 0
        
        for n1, n2 in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            digit = (ord(n1) - ord('0')) + (ord(n2) - ord('0')) + carry
            carry = digit // 10
            val += str(digit % 10)
            
        if carry:
            val += str(carry)
        
        return val[::-1]