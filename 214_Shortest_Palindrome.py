# https://leetcode.com/problems/shortest-palindrome/description/
# Hard

class Solution:
    
    # 1. Find the longest palindrome that includes the first element
    # 2. Then construct the full string by appending the missing characters
    #    to the beginning of the original string.
    #
    # Step 1 can probably be optimized.
    # Full solution is O(n^2) time and O(n) space
    #
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        first = s[0]
        indices = [i for i, x in enumerate(s) if x == first]    # O(n)
        for last in indices[::-1]: # O(n) worst case
            candidate = s[:last+1]
            if candidate == candidate[::-1]: # O(n)
                return s[last+1:][::-1] + s
        return s[::-1] + s

    def shortestPalindrome2(self, s):
        A=s+"*"+s[::-1]
        cont=[0]
        for i in range(1,len(A)):
            index=cont[i-1]
            while(index>0 and A[index]!=A[i]):
                index=cont[index-1]
            cont.append(index+(1 if A[index]==A[i] else 0))
            print(cont)
        return s[cont[-1]:][::-1]+s

s = Solution()
s.shortestPalindrome2("aacecaaa")