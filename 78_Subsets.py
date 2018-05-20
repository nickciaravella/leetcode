# https://leetcode.com/problems/subsets/description/
# Medium

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = [[]]
        self.backtrack(nums, 0, [], solution)
        return solution
    
    def backtrack(self, nums, start, cur, solution):
        for i in range(start, len(nums)):
            cur.append(nums[i])
            solution.append(cur[:])
            self.backtrack(nums, i+1, cur, solution)
            cur.pop()