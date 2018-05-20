# https://leetcode.com/problems/decode-ways/description/
# Medium

class Solution:

    # DP, reduced to two variables
    # Choices are:
    #   Take just the single digit (i.e, 1, 2, 3) and add it to result s[n-1], range = 1-9
    #   Take the double digit (i.e. 12, 13) and add it to result of s[n-2], range = 10-26
    #   If ever encountering n == 0 (i.e. invalid), just return 0
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        nMinus1 = 0
        n = 0
        for i in range(1, len(s)):
            n, nMinus1, nMinus2 = 0, n, nMinus1            
            if int(s[i]) > 0:
                n += nMinus1
            if 10 <= int(s[i-1:i+1]) <= 26:
                n += nMinus2      
            if n == 0:
                return 0

        return n