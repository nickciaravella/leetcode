#
#

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # Heap - add all to the heap, return all back
    def mergeKListsPQ(self, lists):
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        root = ListNode(0)
        current = root
        while heap:
            current.next = ListNode(heapq.heappop(heap))
            current = current.next
        return root.next

    # Divide and conquer
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists)-1, 2):
                new_list.append(self.mergeLists(lists[i], lists[i+1]))
            if len(lists) % 2 == 1:
                new_list.append(lists[-1])
            lists = new_list
        return lists[0] if lists else None
    
    def mergeLists(self, list1, list2):        
        root = ListNode(0)
        current = root
        while current:
            if not list1:
                current.next = list2
                break
            elif not list2:
                current.next = list1
                break
            elif list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next        
        return root.next