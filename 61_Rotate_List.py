# https://leetcode.com/problems/rotate-list/description/
# Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Move linked list into an array
# Do rotation in the array
# Move array back to linked list
# O(n) time, O(n) space, easier to do and understand
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        rotation = k % len(arr)
        rotated = arr[-rotation:] + arr[:-rotation]
                
        head = ListNode(rotated[0])
        current = head
        for num in rotated[1:]:
            current.next = ListNode(num)
            current = current.next
        
        return head

# Count elements in linked list, connect tail to head making a circle
# Starting at the head, skip elements
# Disconnect new tail and return new head
# O(n) time, O(1) space, little harder to read and maintain
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # Form a circle while counting elements
        current, length = head, 1
        while current.next:
            length += 1
            current = current.next
        current.next = head
        
        # Rotate out the last (k % length) elements
        # to the beginning
        skip = length-(k % length)

        prev, current = current, head
        for i in range(skip):
            prev = prev.next
            current = current.next
        
        prev.next = None
        return current