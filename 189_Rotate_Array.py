# https://leetcode.com/problems/rotate-array/description/
# Easy

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        rotated = nums[-k:] + nums[:-k]        
        for i in range(len(nums)):            
            nums[i] = rotated[i]
            
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        cpy = nums[:]
        for i in range(n):            
            nums[i] = cpy[(n-k+i) % n]    