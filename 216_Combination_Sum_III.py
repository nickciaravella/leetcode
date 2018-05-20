# https://leetcode.com/problems/combination-sum-iii/description/
# Medium

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k==0 and n==0:
            return [[]]
        
        numbers = [1,2,3,4,5,6,7,8,9]
        result = []
        for i in range(len(numbers)):            
            self.backtrack(numbers, k, n, numbers[i], i+1, [numbers[i]], result)
        return result
    
    def backtrack(self, numbers, target_count, target, current, start_index, current_result, result):
        if target_count == len(current_result) and target == current:
            result.append(current_result[:])
            return
        if target_count <= len(current_result) or current > target:
            # pruning...
            return
        
        for i in range(start_index, len(numbers)):
            if current+numbers[i] > target:
                # pruning.. 
                break
            current_result.append(numbers[i])
            self.backtrack(numbers, target_count, target, current+numbers[i], i+1, current_result, result)
            current_result.pop()