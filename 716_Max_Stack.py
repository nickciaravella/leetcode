# https://leetcode.com/problems/max-stack/description/
# Hard

from collections import deque

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.max_stack = deque()

    # O(1)
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            cur_max = self.max_stack.pop()
            self.max_stack.append(cur_max)
            if x >= cur_max:
                self.max_stack.append(x)
        
        self.stack.append(x)

    # O(1)
    def pop(self):
        """
        :rtype: int
        """
        val = self.stack.pop()
        
        cur_max = self.max_stack.pop()
        if val != cur_max:
            self.max_stack.append(cur_max)

        return val

    # O(1)
    def top(self):
        """
        :rtype: int
        """
        val = self.stack.pop()
        self.stack.append(val)
        return val

    # O(1)
    def peekMax(self):
        """
        :rtype: int
        """
        val = self.max_stack.pop()
        self.max_stack.append(val)
        return val
        
    # O(n)
    def popMax(self):
        """
        :rtype: int
        """
        cur_max = self.max_stack.pop()

        popped = deque()

        cur = self.stack.pop()
        while cur != cur_max:
            popped.append(cur)
            cur = self.stack.pop()

        while popped:
            self.push(popped.pop())
        
        return cur_max




# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()