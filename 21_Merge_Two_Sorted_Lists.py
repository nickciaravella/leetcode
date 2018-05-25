# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Dummy starting node, avoids checks for
        # which node is the root of the merged list.
        dummy = ListNode(None)
        
        lastNodeOfMerged = dummy        
        while True:
            # If either list is empty, then just append the other list
            # and the merge is complete.
            if not list1:
                lastNodeOfMerged.next = list2
                break
            if not list2:
                lastNodeOfMerged.next = list1
                break
                
            # Choose the smaller list's current node. Then move
            # that list forward to its next node.
            if list1.val <= list2.val:
                lastNodeOfMerged.next = list1
                list1 = list1.next
            else:
                lastNodeOfMerged.next = list2
                list2 = list2.next
            
            # Advance the merged lists node since we added a new
            # node in the previous step.
            lastNodeOfMerged = lastNodeOfMerged.next
        
        return dummy.next  