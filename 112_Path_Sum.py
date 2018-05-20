# https://leetcode.com/problems/path-sum/description/
# Easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum, current=0):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        current = current + root.val

        return ((root.left is None and root.right is None and current == sum) or
                self.hasPathSum(root.left, sum, current) or
                self.hasPathSum(root.right, sum, current))