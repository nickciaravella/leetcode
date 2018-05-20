# https://leetcode.com/problems/combination-sum/description/
# Medium

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        for i, num in enumerate(candidates):
            self.backtrack(candidates, [num], i, target-num, result)
        return result

    def backtrack(self, candidates, arr, start_index, target, solution):  
        if target == 0:
            solution.append(arr)
        elif target < 0:
            return
        else:
            for i in range(start_index, len(candidates)):
                self.backtrack(candidates, arr+[candidates[i]], i, target-candidates[i], solution)