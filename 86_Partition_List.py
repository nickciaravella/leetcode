# https://leetcode.com/problems/partition-list/description/
# Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        larger = ListNode(None)
        larger_head = larger
        smaller = ListNode(None)
        smaller_head = smaller
        
        current = head
        while current:
            if current.val < x:
                smaller.next = current
                smaller = current
            else:
                larger.next = current
                larger = current
            current = current.next
            
        smaller.next = larger_head.next
        larger.next = None
        
        return smaller_head.next        