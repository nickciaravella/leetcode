# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Easy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def find_ancestors(self, root, node):
        """
        :type root: TreeNode
        :type node: TreeNode
        :rtype: List(TreeNode)
        """
        current = root
        stack = []
        while True:
            stack.append(current)
            if node.val == current.val:                
                return stack
            elif node.val < current.val:
                current = current.left
            else:
                current = current.right                

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stackp = self.find_ancestors(root, p)
        stackq = self.find_ancestors(root, q)

        for i in range(len(stackp)-1, 0, -1):
            if i >= len(stackq):
                continue
            if stackp[i].val == stackq[i].val:
                return stackp[i]

        return root

# Traverse until they diverge (since its a binary SEARCH tree)
class Solution(object):            
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while True:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root        