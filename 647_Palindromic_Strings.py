# https://leetcode.com/problems/palindromic-substrings/description/
# Medium

class Solution:    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """        
        return sum(1 for start in range(len(s)) for end in range(start+1, len(s)+1) if s[start:end] == s[start:end][::-1])