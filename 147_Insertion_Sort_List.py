#
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        sorted_head = ListNode(head.val)
        
        insert_current = head.next
        while insert_current is not None:
            sorted_head = self.insert_node(sorted_head, ListNode(insert_current.val))
            insert_current = insert_current.next
        return sorted_head

    def insert_node(self, head, node):
        if node.val < head.val:
            node.next = head
            return node
        
        prev = head
        current = head.next
        while current is not None:
            if node.val < current.val:
                node.next = current
                break
            else:
                prev = current
                current = current.next
        
        prev.next = node
        return head


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(2)
node4 = ListNode(0)
node1.next = node2
node2.next = node3
node3.next = node4

print ("UNSORTED")
current = node1
while current is not None:
    print(current.val)
    current = current.next

s = Solution()
current = s.insertionSortList(node1)

print ("SORTED")
while current is not None:
    print(current.val)
    current = current.next


