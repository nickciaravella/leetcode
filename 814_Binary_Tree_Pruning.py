# https://leetcode.com/problems/binary-tree-pruning/description/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        root.left = self.pruneTree(root.left) 
        root.right = self.pruneTree(root.right)
                        
        return root if root.left or root.right or root.val == 1 else None