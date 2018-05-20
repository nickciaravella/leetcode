# https://leetcode.com/problems/minimum-window-substring/description/
# Hard

from collections import Counter

class Solution:
    def minWindow(self, string, needed):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needed_letter_counts = Counter(needed)
        needed_letters = len(needed_letter_counts)
        window = (0,0)
        
        start = end = 0
        while end < len(string):            
            char = string[end]
            if char in needed_letter_counts:
                needed_letter_counts[char] -= 1
                if needed_letter_counts[char] == 0:
                    needed_letters -= 1
            end += 1
            
            while start < end and needed_letters == 0 :
                if window[1]-window[0] > end-start or window == (0,0):
                    window = (start, end)
                
                char = string[start]
                if char in needed_letter_counts and needed_letter_counts[char] == 0:
                    break
                elif char in needed_letter_counts:
                    needed_letter_counts[char] += 1                    
                start += 1

        return string[window[0]:window[1]]