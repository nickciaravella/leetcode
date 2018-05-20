# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Medium

from bisect import bisect_left

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        # find pivot point, smallest element
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        
        smallest = low
        
        # binary search from smallest to end
        pos = bisect_left(nums, target, smallest, len(nums))
        if pos < len(nums) and nums[pos] == target:
            return pos
        
        # binary search from start to smallest-1
        pos = bisect_left(nums, target, 0, smallest)
        if pos < len(nums) and nums[pos] == target:
            return pos
        
        return -1