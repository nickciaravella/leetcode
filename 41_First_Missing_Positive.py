# https://leetcode.com/problems/first-missing-positive/description/
# Hard

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        for i in range(len(nums)):
            cur = nums[i]
            while cur >= 0 and cur < len(nums) and nums[cur] != cur:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur = nums[i]
            
        print(nums)
        for i in range(1, len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)
