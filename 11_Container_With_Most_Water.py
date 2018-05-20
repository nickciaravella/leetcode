# https://leetcode.com/problems/container-with-most-water/description/
# Medium

# 2 pointers - O(n)
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, maximum = 0, len(height)-1, 0
        while left != right:
            maximum = max(maximum, (right-left) * min(height[right], height[left]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maximum

# Dynamic Programming - Time limit exceeded, O(n^2)
class SolutionDp:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return max(x2 * min(y1, y2) for x1, y1 in enumerate(height) for x2, y2 in enumerate(height[x1:]))
