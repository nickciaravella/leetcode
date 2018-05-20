# https://leetcode.com/problems/valid-palindrome-ii/description/
# Easy

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, lambda left, right: self.isPalindrome(s[left+1:right+1]) or self.isPalindrome(s[left:right]))
            
    def isPalindrome(self, s, error=lambda x,y: False):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return error(left, right)
            left += 1
            right -= 1
        return True
