# https://leetcode.com/problems/roman-to-integer/description/
# Easy

# Symbol	I	V	X	 L	C	     D	      M
#Value	    1	5	10 	50	100 	500 	1,000

class Solution:

    charToNum = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        total = 0
        for numeral in s[::-1]:
            cur = self.charToNum[numeral]
            total += cur if cur >= prev else -1*cur
            prev = cur
        return total
