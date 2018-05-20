# https://leetcode.com/problems/plus-one/description/
# Easy

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ret = []
        carry = 1
        for val in digits[::-1]:
            next_val = val + carry
            carry = next_val // 10
            next_val = next_val % 10
            ret.insert(0, next_val)
        
        if carry > 0:
            ret.insert(0, carry)
        
        return ret

s = Solution()
print(s.plusOne([9, 9, 9, 9]))
print(s.plusOne([9, 9, 5, 9]))