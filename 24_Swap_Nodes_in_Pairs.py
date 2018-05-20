# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.makeSwap(head)

    def makeSwap(self, head):
        first = head         
        if first is None or first.next is None:
            return first           
        second = head.next
        third = head.next.next
        second.next = first
        first.next = self.makeSwap(third)
        return second
        