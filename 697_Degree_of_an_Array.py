# https://leetcode.com/problems/degree-of-an-array/description/
# Easy

from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        first_indicies = defaultdict(int)
        max_freq = 0
        min_sub = 0
        
        for i, num in enumerate(nums):            
            if num not in first_indicies:
                first_indicies[num] = i
            
            counts[num] += 1
            
            # Update our max degree and set new smallest sub-array
            if counts[num] > max_freq:
                max_freq = counts[num]
                min_sub = i-first_indicies[num]+1
            # Update our smallest sub-array if == to max degree
            elif counts[num] == max_freq:
                min_sub = min(min_sub, i-first_indicies[num]+1)
                
        return min_sub