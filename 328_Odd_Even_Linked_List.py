# https://leetcode.com/problems/odd-even-linked-list/description/
# Medium

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        even_head = head
        odd_head = head.next

        current = odd_head
        current_pos = 1

        odd_current = odd_head
        even_current = even_head
        while current.next != None:
            if current_pos % 2 == 1:
                even_current.next = current.next
                even_current = even_current.next
            elif current_pos % 2 == 0:
                odd_current.next = current.next
                odd_current = odd_current.next
            current = current.next
            current_pos += 1

        odd_current.next = None
        even_current.next = odd_head
        return even_head