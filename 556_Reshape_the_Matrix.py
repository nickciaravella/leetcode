# https://leetcode.com/problems/reshape-the-matrix/description/
# Easy

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        
        elements = len(nums) * len(nums[0])
        if r*c != elements:
            return nums
        
        matrix = [[]]
        for row in nums:
            for num in row:
                if len(matrix[-1]) == c:
                    matrix.append([])
                matrix[-1].append(num)
                
        return matrix