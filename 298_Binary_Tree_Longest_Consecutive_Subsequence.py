# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
# Medium

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recurse(root)[1]
    
    def recurse(self, root):
        if not root:
            return 0, 0
        
        left, left_longest = self.recurse(root.left)
        right, right_longest = self.recurse(root.right)
        
        if root.left and root.val == root.left.val-1:
            left += 1
        else:
            left = 1
            
        if root.right and root.val == root.right.val-1:
            right += 1
        else:
            right = 1
            
        return max([left, right]), max([left, right, left_longest, right_longest])
        