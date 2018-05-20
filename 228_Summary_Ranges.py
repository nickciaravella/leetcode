# https://leetcode.com/problems/summary-ranges/description/
# Medium

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        range_start = nums[0]
        prev = nums[0]
        ranges = []
        for num in nums[1:] + [nums[0]]:
            if num != prev+1:
                if range_start == prev:
                    ranges.append(str(range_start))
                else:
                    ranges.append(str(range_start) + "->" + str(prev))
                range_start = num
            prev = num
        return ranges
