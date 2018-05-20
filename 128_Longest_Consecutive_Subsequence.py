# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Hard

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        
        longest = 0
        for num in nums:
            if num-1 in numset:
                # this is the midde of a sequence
                continue
                
            current_longest = 1
            current_num = num
            while current_num+1 in numset:
                current_longest += 1
                current_num += 1
            longest = max(longest, current_longest)
            
        return longest