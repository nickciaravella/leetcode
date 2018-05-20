# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        arr = []
        self.fill_array(root, arr)
        
        root = arr[0]
        root.left = None
        root.right = None

        i = 1
        current = root
        while i < len(arr):
            current.right = arr[i]
            current = arr[i]
            current.left = None
            current.right = None
            i += 1
    

    def fill_array(self, root, arr):
        if root is None:
            return
        arr.append(root)
        self.fill_array(root.left, arr)        
        self.fill_array(root.right, arr)
