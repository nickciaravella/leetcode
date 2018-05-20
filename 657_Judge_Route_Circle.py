# https://leetcode.com/problems/judge-route-circle/description/
# Easy

from collections import Counter
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counter = Counter(moves)
        return counter['L'] == counter['R'] and counter['U'] == counter['D']


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical, horizontal = 0, 0        
        for letter in moves:
            if letter == 'L': horizontal -=1
            elif letter == 'R': horizontal += 1
            elif letter == 'U': vertical += 1
            else: vertical -= 1
        return vertical == 0 and horizontal == 0