# https://leetcode.com/problems/reverse-linked-list/description/
# Easy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        stack = []        
        current == head
        while current != None:
            stack.append(current)
            current = current.next

        root = stack.pop()
        current = root
        while len(stack) > 0:
            current.next = stack.pop()
            current = current.next
        
        current.next = None

        return root

        