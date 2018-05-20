# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
# Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Convert linked list to an array, then re-use solution
    # from 108_Convert_Sorted_Array_To_Binary_Search_Tree
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.recurse(nums, 0, len(nums)-1)

    def recurse(self, nums, low, high):
        if high < low:
            return         
        current = (low+high+1)//2
        root = TreeNode(nums[current])
        root.left = self.recurse(nums, low, current-1)
        root.right = self.recurse(nums, current+1, high)
        return root