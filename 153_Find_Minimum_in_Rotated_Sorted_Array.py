# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Medium

# Too complicated - BFS binary search
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        low = 0
        mid = len(nums) // 2
        high = len(nums)-1
        stack = [(low, mid, high)]
        while len(stack) > 0:
            low, mid, high = stack.pop()
            if low > mid or low > high or mid > high:
                continue

            if nums[mid-1] > nums[mid] and (mid+1 == len(nums) or nums[mid+1] > nums[mid]):
                return nums[mid]
            else:
                stack.append((mid+1, (mid+high+1)//2, high))                
                stack.append(((low, (low+mid-1)//2, mid-1)))
        return nums[0]
