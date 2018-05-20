# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Can optimize space by:
# Only store the answer
# Traverse right to left and keep only the first element per level
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []
        self.populate(root, 0, tree)
        return [row[-1] for row in tree]
        
    def populate(self, root, level, tree):
        if not root:
            return
        
        if len(tree) <= level:
            tree.append([])
        
        tree[level].append(root.val)
        self.populate(root.left, level+1, tree)
        self.populate(root.right, level+1, tree)