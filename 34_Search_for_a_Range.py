# https://leetcode.com/problems/search-for-a-range/description/
# Medium

# Two binary search approach. If statements can be simplified a bit.
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.find_boundary(nums, target, True), self.find_boundary(nums, target, False)]
        
    def find_boundary(self, nums, target, isStart):
        start, end = 0, len(nums)-1
        offset = -1 if isStart else 1
        boundary = start if isStart else end
        
        while start <= end:
            middle = (start+end)//2
            if nums[middle] == target:                
                if middle == boundary or nums[middle+offset] != target:
                    return middle
                elif isStart:
                    end = middle-1
                else:
                    start = middle+1
            elif nums[middle] > target:
                end = middle-1
            else:
                start = middle+1
        return -1