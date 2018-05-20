# https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
# Medium

class Solution:
    def reverseWords(self, string):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """        
        cur = ''
        stack = []
        for letter in string:
            if letter == ' ':
                if cur:
                    stack.append(cur)
                stack.append(' ')
                cur = ''
            else:
                cur += letter
        if cur:
            stack.append(cur)

        index = 0
        while stack:
            word = stack.pop()
            for letter in word:
                string[index] = letter
                index += 1