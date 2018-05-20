# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
# Easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution is copied from 102_Binary_Tree_Level_Order_Traversal, just added the reversal at the end.
class Solution:
    # Breadth-first traversal using queue
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop()
            if node is None:
                continue

            if len(result) < depth:
                result.append([])            
            result[depth-1].append(node.val)

            queue.insert(0, (node.left, depth+1))
            queue.insert(0, (node.right, depth+1))
        
        return result.reverse()