# https://leetcode.com/problems/subarray-sum-equals-k/description/
# Medium

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = total = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for i in range(len(nums)):                        
            total += nums[i]
            count += prefix[total-k]
            prefix[total] += 1                        
        return count