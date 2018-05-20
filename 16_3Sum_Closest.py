# https://leetcode.com/problems/3sum-closest/description/
# Medium

class Solution(object):
    
    # O(n^2)
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 'Invalid'
        
        nums.sort() 
        closest = nums[0] + nums[1] + nums[2]
        for i, num1 in enumerate(nums[0:-2]):
            j = i+1
            k = len(nums)-1            
            while j < k:
                num2, num3 = nums[j], nums[k]
                new_sum = num1+num2+num3
                if new_sum == target:
                    return target
                if abs(target-closest) > abs(target-new_sum):
                    closest = new_sum
                
                if new_sum > target:
                    k-=1
                else:
                    j+=1
        return closest
        
    # O(n^3)     
    def threeSumClosestBacktracking(self, nums, target):    
        return self.backtrack(nums, target, None, 0, 0)
    
    def backtrack(self, nums, target, min_sum, cur_sum, count):
        if count > 3:
            return min_sum
        if count == 3 and (min_sum is None or abs(target - cur_sum) < abs(target - min_sum)):
            min_sum = cur_sum
            return min_sum
        
        for i, val in enumerate(nums):
            cur_sum += val
            count += 1
            
            min_sum = self.backtrack(nums[i+1:], target, min_sum, cur_sum, count)
                
            cur_sum -= val
            count -= 1
        
        return min_sum