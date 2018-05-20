#
#

from collections import Counter

class Solution:

    # Backtracking solution - results in stack being too large
    # Thought:
    #   if count of all characters > k : return len(string)
    #   else return max(s[1:end], s:[:end-1])
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counts = Counter(s)        
        return self.backtrack(s, k, 0, len(s)-1, counts, {})
                        
    def backtrack(self, s, k, start, end, counts, memo):        
        if ((start, end) in memo):
            return memo[(start, end)]
        
        if end-start+1 < k:
            return 0
                
        if all(counts[c] >= k or counts[c] == 0 for c in counts):
            memo[(start, end)] = end-start+1
            return end-start+1
        
        counts[s[start]] -= 1
        minusFirst = self.backtrack(s, k, start+1, end, counts, memo)
        counts[s[start]] += 1
        
        counts[s[end]] -= 1
        minusLast = self.backtrack(s, k, start, end-1, counts, memo)
        counts[s[end]] += 1
        
        ret = max(minusFirst, minusLast)
        memo[(start, end)] = ret
        return ret