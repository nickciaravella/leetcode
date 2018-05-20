# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# Medium

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while True:
            middle = (high+low)//2
            #print("h="+str(high)+", l="+str(low)+", m="+str(middle))
            
            if middle-1 >= 0 and nums[middle] == nums[middle-1]:
                if middle % 2 == 0:
                    high = middle-1
                else:
                    low = middle+1
            elif middle+1 < len(nums) and nums[middle] == nums[middle+1]:
                if middle % 2 == 0:
                    low = middle+1
                else:
                    high = middle-1
            else:
                return nums[middle]