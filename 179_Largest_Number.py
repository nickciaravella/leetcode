# https://leetcode.com/problems/largest-number/description/
# Medium

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(lambda num: str(num), nums)
        sorted_nums = sorted(nums, key=cmp_to_key(is_larger), reverse=True)
        return str(int(''.join(sorted_nums)))


def is_larger(num1, num2):
        if int(num1+num2) > int(num2+num1):
            return 1
        else:
            return -1
        