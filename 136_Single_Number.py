# https://leetcode.com/problems/single-number/description/
# Easy

import functools as f

class Solution2:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = set()
        removed = set()
        for num in nums:
            if num in removed:
                return num
            elif num in lookup:
                lookup.remove(num)
                removed.add(num)
            else:
                lookup.add(num)
        return lookup.pop()

class Solution1:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        for num in nums:
            lookup[num] = 1 if num not in lookup else lookup[num] + 1
        for num in lookup.keys():
            if lookup[num] != 2:
                return num
        raise ValueError("No number that didn't appear exactly twice.")

class SolutionWithTheTrick:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return f.reduce((lambda x, y: x^y), nums, 0)
