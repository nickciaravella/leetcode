# https://leetcode.com/problems/repeated-dna-sequences/description/
# Medium

# Solution can be improved by creating your own hash algorithm for
# a 10 char string. Then simply alter it in O(1) time by removing first
# character and appending the next one. This would be faster than
# creating a slice in each iteration.

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        
        repeated = set()
        seen = set()
        result = []
        start = 0
        end = 10
        
        while end <= len(s):
            candidate = s[start:end]
            if candidate in seen:
                repeated.add(candidate)
            else:
                seen.add(candidate)
            start += 1
            end += 1
        
        return list(repeated)