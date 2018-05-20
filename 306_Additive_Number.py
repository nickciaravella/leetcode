# https://leetcode.com/problems/additive-number/description/
# Medium


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, len(num)-1):
            for j in range(i+1, len(num)):
                if self.recurse(num[:i], num[i:j], num[j:]):
                    return True
        return False
        
    def recurse(self, first, second, rest):        
        if not rest:
            return False
        
        if not rest.startswith(str(int(first)+int(second))):
            return False
        
        if ((first.startswith('0') and len(first) > 1)   or
            (second.startswith('0') and len(second) > 1) or
            (rest.startswith('0') and len(rest) > 1)):
            return False
        
        if int(first)+int(second) == int(rest):
            return True
        
        # This part is slow - looking at all possible new second values
        for i in range(1, len(rest)):
            new_first, new_second, new_rest = second, rest[:i], rest[i:]
            if self.recurse(new_first, new_second, new_rest):
                return True
            
        return False


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, len(num)-1):
            for j in range(i+1, len(num)):
                if self.recurse(num[:i], num[i:j], num[j:]):
                    return True
        return False
        
    def recurse(self, first, second, rest):        
        if not rest:
            return True
        
        if not rest.startswith(str(int(first)+int(second))):
            return False
        
        # Rule out invalid numbers, they cannot start with 0 unless they are 0
        # 03 for example is invalid
        if ((first.startswith('0') and len(first) > 1)   or
            (second.startswith('0') and len(second) > 1) or
            (rest.startswith('0') and len(rest) > 1)):
            return False
        
        # Optimized - Once the first and second and chosen and valid,
        # there is no choice for the next first and second. The must
        # be first = second, second = first + second
        nxt = str(int(first)+int(second))
        return self.recurse(second, rest[:len(nxt)], rest[len(nxt):])      