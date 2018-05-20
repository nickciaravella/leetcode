# https://leetcode.com/problems/binary-search-tree-iterator/description/
# Medium

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Original version
class BSTIterator(object):

    _stack = []
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._current = root        
        if self._current != None:
            self.traverse_left()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._current != None

    def next(self):
        """
        :rtype: int
        """
        val = self._current.val

        if self._current.right != None:
            self._current = self._current.right
            self.traverse_left()
        elif len(self._stack) > 0 :
            self._current = self._stack.pop()
        else:
            self._current = None

        return val
        
    def traverse_left(self):
        while self._current.left != None:
            self._stack.append(self._current)
            self._current = self._current.left

# Simplified version
class BSTIterator(object):

    _stack = []
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.traverse_left(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self._stack) > 0

    def next(self):
        """
        :rtype: int
        """
        current = self._stack.pop()
        self.traverse_left(current.right)
        return current.val
        
    def traverse_left(self, current):
        while current is not None:
            self._stack.append(current)
            current = current.left