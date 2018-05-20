# https://leetcode.com/problems/path-sum-ii/description/ 
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.pathSum2(root, sum, 0, [], result)
        return result

    def pathSum2(self, root, sum, cur, path, result):
        if root is None:
            return

        cur = cur + root.val
        path.append(root.val)

        if cur == sum and root.left is None and root.right is None:
            result.append(path[:])
        
        self.pathSum2(root.left, sum, cur, path, result)
        self.pathSum2(root.right, sum, cur, path, result)
        path.pop()