# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Medium

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def dfs(self, root, node):
        stack = [root]
        parentMap = {}

        found = None
        while stack:
            top = stack.pop()   
                    
            if top == node:
                found = top
                break

            if top.left:
                parentMap[top.left] = top
                stack.append(top.left)
            if top.right:
                parentMap[top.right] = top
                stack.append(top.right)
        
        path = [found]
        child = found
        while child in parentMap:
            path.insert(0, parentMap[child])
            child = parentMap[child]

        return path

    # DFS solution - O(n^2)
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        dfsStackP = self.dfs(root, p)
        print (dfsStackP)
        dfsStackQ = self.dfs(root, q)
        print (dfsStackQ)
        prev = None
        for anp, anq in zip(dfsStackP, dfsStackQ):
            if anp != anq:
                return prev
            prev = anp
        return prev

    # Recursive solution - O(n)
    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
