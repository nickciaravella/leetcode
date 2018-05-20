# https://leetcode.com/problems/string-compression/description/
# Easy

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        # cur - where to insert into array
        # slow - start of new letter
        # fast - count through all of letter
        
        cur = slow = fast = 0
        while fast < len(chars):
            
            # count how many letters
            count = 0
            while fast < len(chars) and chars[slow] == chars[fast]:
                count += 1
                fast += 1
                
            # write letter
            chars[cur] = chars[slow]
            cur += 1
            
            # write count if > 1
            if count > 1:
                for letter in str(count):
                    chars[cur] = letter
                    cur += 1
            
            # move to next letter
            slow = fast
                                
        return cur