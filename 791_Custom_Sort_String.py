# https://leetcode.com/problems/custom-sort-string/description/
# Medium

from collections import Counter

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counts = Counter(T)        
        
        result = ""
        for char in S:
            result += (char*counts[char])
            del counts[char]
        
        for char, count in counts.items():
            result += (char*counts[char])
            
        return result