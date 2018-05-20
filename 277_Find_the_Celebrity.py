# https://leetcode.com/problems/find-the-celebrity/description/
# Medium

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# First pass - find a candidate
# Second pass - verify
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celebrity = 0
        for guest in range(1, n):
            if knows(celebrity, guest):
                celebrity = guest
        for guest in range(n):
            if guest != celebrity and (knows(celebrity, guest) or not knows(guest, celebrity)):
                return -1
        return celebrity
                