# https://leetcode.com/problems/maximum-binary-tree/description/
# Medium

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        pivot = nums.index(max(nums))
        root = TreeNode(nums[pivot])
        root.left = self.constructMaximumBinaryTree(nums[:pivot])
        root.right = self.constructMaximumBinaryTree(nums[pivot+1:])
        return root