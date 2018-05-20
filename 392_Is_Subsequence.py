# https://leetcode.com/problems/is-subsequence/description/
# Medium

# Recursion - finds the first subsequence. (optimized O(n^2))
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
                
        for i, c in enumerate(t):
            if c == s[0] and self.isSubsequence(s[1:], t[i+1:]):
                return True
        return False
    
# DP - O(n^2)
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp = [[True]*(len(t)+1) for i in range(len(s)+1)]
            
        for i in range(1, len(s)+1):
            dp[i][0] = False
            for j in range(1, len(t)+1):
                dp[i][j] = (s[i-1] == t[j-1] and dp[i-1][j-1]) or dp[i][j-1]
     
        return dp[-1][-1]