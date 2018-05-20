# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        
        return result

    # In-order traversal using recursion
    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.levelOrder2_recurse(root, 0, result)
        return result
    
    def levelOrder2_recurse(self, root, depth, result):
        if root is None:
            return
        if len(result) <= depth:
            result.append([])

        self.levelOrder2_recurse(root.left, depth+1, result)
        result[depth].append(root.val)
        self.levelOrder2_recurse(root.right, depth+1, result)