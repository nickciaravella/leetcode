# https://leetcode.com/problems/string-to-integer-atoi/description/
# Medium

from itertools import takewhile

class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        # Remove whitespace
        trimmed = string.strip()
        if not trimmed:
            return 0
        
        # Handle string starting with '-' or '+' sign
        negative_factor = 1
        if trimmed[0] == '-' or trimmed[0] == '+':
            negative_factor = -1 if trimmed[0] == "-" else 1
            trimmed = trimmed[1:]
        
        # Take the leading digits and ignore ending non-digits (valid)
        numbers = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
        digits = list(takewhile(lambda char: char in numbers, trimmed))
        
        # Convert the string to a number (not using int() on purpose)
        converted = 0
        factor = 1
        for i,digit in enumerate(reversed(digits)):
            converted += (numbers[digit]*factor)
            factor *= 10
            if converted > 2147483648:
                # We've crossed the max/min boundary
                break

        # Apply leading positive/negative sign
        converted *= negative_factor
        
        # Return converted number or max/min values
        if converted < -2147483648:
            return -2147483648
        elif converted > 2147483647:
            return 2147483647
        else:
            return converted