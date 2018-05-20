# https://leetcode.com/problems/generate-parentheses/description/
# Medium

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        parenthesisSet = {"()"}        
        for i in range(1, n):
            parenthesisSet = { parenthesis[:i] + "()" + parenthesis[i:] for parenthesis in parenthesisSet for i in range(len(parenthesis))  }            
        return list(parenthesisSet)
