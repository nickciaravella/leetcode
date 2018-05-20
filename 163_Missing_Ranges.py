# https://leetcode.com/problems/missing-ranges/description/
# Medium

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ranges = []
        nums.append(upper+1)
        
        prev = lower-1        
        for cur in nums:
            if cur - prev == 2:
                ranges.append(str(cur-1))
            elif cur - prev > 2:
                ranges.append(str(prev+1)+'->'+str(cur-1))
            prev = cur
        
        return ranges