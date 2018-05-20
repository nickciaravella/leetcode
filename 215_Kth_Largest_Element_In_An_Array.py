# https://leetcode.com/problems/kth-largest-element-in-an-array 
# Medium

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = list(map(lambda x: -1*x, nums))
        heapq.heapify(max_heap)
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        return -1 * heapq.heappop(max_heap) 
    