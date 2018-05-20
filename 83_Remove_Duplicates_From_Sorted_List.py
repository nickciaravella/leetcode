# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Easy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        prev, cur = head, head.next
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return head
        