# https://leetcode.com/problems/add-two-numbers-ii/description/
# Medium

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Easy solution, O(n) time and O(n) space
# Convert linked lists to strings
# Convert strings to ints for sum
# Convert sum back to linked list for return
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1, val2 = "", ""
        while l1:        
            val1 += str(l1.val)
            l1 = l1.next
        while l2:
            val2 += str(l2.val)
            l2 = l2.next
        
        res = int(val1)+int(val2)
        nxt = None
        while res != 0:
            cur = ListNode(res%10)
            cur.next = nxt
            nxt = cur
            res //= 10
        
        return nxt if nxt else [0]

# More complex solution, O(n) time and O(1) space (excluding returned list)
# Reverse both linked lists
# Create sum list by iterating through both lists
# Reverse summed list
#
# Trade-off: This modifies the original lists. Can use stack (O(n) space) or above solution otherwise.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root1, root2 = self.reverse(l1), self.reverse(l2)

        carry = 0
        current1, current2 = root1, root2
        res_sent = ListNode(0)
        res_current = res_sent
        while current1 or current2 or carry:            
            val1 = current1.val if current1 else 0
            val2 = current2.val if current2 else 0

            res = val1 + val2 + carry
            res_current.next = ListNode(res%10)            
            carry = res//10

            res_current = res_current.next
            current1 = current1.next if current1 else current1
            current2 = current2.next if current2 else current2
            
        return self.reverse(res_sent.next)


    def reverse(self, root):
        current, prev, root.next = root.next, root, None
        while current:
            temp = current.next
            current.next, prev, current = prev, current, temp
        return prev


# l1 = ListNode(7)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# l1.next.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# s = Solution()
# rev = s.addTwoNumbers(l1,l2)
# while rev:
#     print(rev.val)
#     rev = rev.next