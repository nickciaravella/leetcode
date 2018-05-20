#
#

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "*": lambda x,y: x*y,
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: float(x)/y
        }

        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                result = operations[token](val2, val1)
                stack.append(int(result))
        return stack.pop()


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))