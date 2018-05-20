# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Easy 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next != None:
            node.val = node.next.val
            if node.next.next == None:
                node.next = None
            else:
                node = node.next
            node = None
            

        

            