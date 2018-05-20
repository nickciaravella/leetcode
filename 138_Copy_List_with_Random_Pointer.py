# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Medium

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None

        mapping = {}
        
        current = head  
        copy_head = RandomListNode(current.label)
        copy_current = copy_head
        
        # Deep copy of nodes, maintain mapping
        mapping[current] = copy_current
        current = current.next
        while current != None:
            copy_current.next = RandomListNode(current.label)
            copy_current = copy_current.next
            mapping[current] = copy_current
            current = current.next

        current = head
        copy_current = copy_head
        while current != None:
            if current.random != None:
                copy_current.random = mapping[current.random]
            current = current.next
            copy_current = copy_current.next
                
        return copy_head    