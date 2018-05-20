# https://leetcode.com/problems/maximum-subarray/description/
# Easy

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = ret = nums[0]
        for num in nums[1:]:
            cur = max(cur+num, num)
            ret = max(cur, ret)
        return ret
