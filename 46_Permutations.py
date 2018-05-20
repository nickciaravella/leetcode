# https://leetcode.com/problems/permutations/description/
# Medium

# Gives me a headache
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(nums, len(nums), result)
        return result
    
    def backtrack(self, nums, element_to_move, result):
        if element_to_move == 1:
            result.append(nums[:])
        
        for i in range(element_to_move):
            nums[i], nums[element_to_move-1] = nums[element_to_move-1], nums[i]
            self.backtrack(nums, element_to_move-1, result)
            nums[i], nums[element_to_move-1] = nums[element_to_move-1], nums[i]
            