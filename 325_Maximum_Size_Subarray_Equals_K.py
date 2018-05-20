# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
# Medium

class Solution(object):
    
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {}
        cur_sum = 0
        max_len = 0
        for i, num in enumerate(nums):
            cur_sum += num
            
            if cur_sum == k:
                max_len = i+1
            
            diff = cur_sum - k
            if diff in sums:
                max_len = max(max_len, i-sums[diff])
                            
            if cur_sum not in sums:
                sums[cur_sum] = i

        return max_len