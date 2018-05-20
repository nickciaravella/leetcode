# https://leetcode.com/problems/balanced-binary-tree/description/
# Easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.solve(root, 0)[0]
    
    def solve(self, root, cur_depth):
        if root is None:
            return (True, cur_depth)
        
        balanced_left, depth_left = self.solve(root.left, cur_depth+1)
        balanced_right, depth_right = self.solve(root.right, cur_depth+1)
        return (balanced_left and balanced_right and abs(depth_left-depth_right) < 2, max(depth_left, depth_right))
            