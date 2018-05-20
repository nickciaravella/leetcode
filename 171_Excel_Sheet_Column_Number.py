# https://leetcode.com/problems/excel-sheet-column-number/description/
# Easy

class Solution:
    def charWeight(self, c):
        return (ord(c)-ord('A'))+1
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum((26**i) * self.charWeight(c) for i,c in enumerate(s[::-1]))