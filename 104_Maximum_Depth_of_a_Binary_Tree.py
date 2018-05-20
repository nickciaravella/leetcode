# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Sipmle BFS tree traversal
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        max_depth = 0
        nodes_and_depth = [ (root, 1) ]
        while len(nodes_and_depth) > 0:
            node, depth = nodes_and_depth.pop()
            if node is None:
                continue            
            max_depth = max(max_depth, depth)                        
            nodes_and_depth.append((node.left, depth+1))
            nodes_and_depth.append((node.right, depth+1))
        return max_depth
        