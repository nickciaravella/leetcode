# https://leetcode.com/problems/smallest-range/description/
# Hard

import heapq

# Two pointers solution expanded to k pointers.
# Keep track of the largest element pointed to, this is the right side of the candidate range
# Find the minimum element currently pointed to (storing them in a heap for O(1) access, O(lgk) insert)
# Update min range, move pointer forward one in the array, update largest element
# Two cases where you can stop, a) all smallest == largest, can't get any better than that, b) cannot move smallest forward
#
# Time complexity: O(n * k * lgk)
# every element is inserted into the heap once (n*k elements) taking lgk time on each insert
class Solution:
    
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = [] # heap of current pointers
        largest = nums[0][0] # max element pointed to        
        min_range = [-1*10**5, 10**5] # min range found

        # initialize based on first element of all arrays
        for i,arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            largest = max(largest, arr[0])

        while True:
            # Get the smallest element pointed to
            smallest, arr_index, pos = heapq.heappop(heap)

            # Determine if its a better range            
            if smallest == largest:
                return [smallest, largest]

            if (min_range[1] - min_range[0]) > largest - smallest:
                min_range = [smallest, largest]
        
            # If this array is already at the end, we are done
            if pos == len(nums[arr_index])-1:
                return min_range

            # Move the smallest element forward
            new_element = nums[arr_index][pos+1]
            largest = max(new_element, largest)
            heapq.heappush(heap, (new_element, arr_index, pos+1))


s = Solution()
print(s.smallestRange([
    [4,10,15,24,26],
    [0,10,12,20],
    [5,18,22,30]
    ]))