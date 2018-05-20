# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.recurse(nums, 0, len(nums)-1)

    def recurse(self, nums, low, high):
        if high < low:
            return         
        current = (low+high+1)//2
        root = TreeNode(nums[current])
        root.left = self.recurse(nums, low, current-1)
        root.right = self.recurse(nums, current+1, high)
        return root


s = Solution()
s.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])