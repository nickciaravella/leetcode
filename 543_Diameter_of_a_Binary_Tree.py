# https://leetcode.com/problems/diameter-of-binary-tree/description/
# Easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.diameterFromRoot(root)[1]
    
    def diameterFromRoot(self, root):
        if not root:
            return 0, 0        
        lengthOfLeft, maxFromLeft = self.diameterFromRoot(root.left)
        lengthOfRight, maxFromRight = self.diameterFromRoot(root.right)
        longestPathThroughMe = lengthOfLeft + lengthOfRight
        return max(lengthOfLeft, lengthOfRight)+1, max(maxFromLeft, maxFromRight, longestPathThroughMe)