# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Medium

class Solution:

    lookup = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": " "
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        possibleStrings = ['']
        for digit in digits:     
            possibleStrings = [string + char for char in self.lookup[digit] for string in possibleStrings]
        return possibleStrings
