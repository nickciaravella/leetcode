# https://leetcode.com/problems/number-of-lines-to-write-string/description/
# Easy

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 1
        column = 0
        for c in S:
            width = widths[ord(c)-ord('a')]
            if column+width > 100:
                line += 1
                column = width
            else:
                column += width
        return [line, column]