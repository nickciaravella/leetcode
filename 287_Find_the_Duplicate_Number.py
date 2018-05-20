# https://leetcode.com/problems/find-the-duplicate-number/discuss/
# Medium

# binary search using pigeon hole principle
# O(nlgn)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low = 1
        high = len(nums)-1
        while True:
            mid = (high+low)//2

            count_left = 0
            count_equal = 0
            
            for num in nums:
                if num == mid:
                    count_equal += 1
                if num < mid:
                    count_left += 1
            
            if count_equal > 1:
                return mid
            elif count_left >= mid:
                high = mid-1
            else:
                low = mid+1

        return -1
