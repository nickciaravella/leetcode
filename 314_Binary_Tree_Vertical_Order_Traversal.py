# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
from collections import deque

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mapping = defaultdict(list)
        queue = deque([(root, 0)])
        left, right = 0, 0
        while queue:
            node, col = queue.pop()
            if node:
                mapping[col].append(node.val)
                queue.appendleft((node.left, col-1))
                queue.appendleft((node.right, col+1))
                left = min(left, col)
                right = max(right, col)
                
        return [mapping[i] for i in range(left, right+1)] if mapping else []