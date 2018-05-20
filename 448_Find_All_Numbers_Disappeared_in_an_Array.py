# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Easy

class Solution(object):
    # Replace the numbers in the original array with -1 when they are seen
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [-1] + nums
        
        for i in range(len(nums)):
            j = nums[i]
            while j != -1 and nums[j] != -1:
                temp = nums[j]
                nums[j] = -1
                j = temp
                
        return [i for i, num in enumerate(nums) if num != -1]

# Alteration, little simpler, just make the original numbers negative
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        
        for i, num in enumerate(nums):
            nums[abs(num)] = -1 * abs(nums[abs(num)])
                
        return [i for i, num in enumerate(nums) if num > 0]