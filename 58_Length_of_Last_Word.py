# https://leetcode.com/problems/length-of-last-word/description/
# Easy

class Solution:
    def lengthOfLastWord(self, s):
        words = list(filter(lambda x: len(x) > 0, s.split(' ')))
        return len(words[-1]) if len(words) > 0 else 0
