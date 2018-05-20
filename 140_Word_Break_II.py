# https://leetcode.com/problems/word-break-ii/description/
# Hard

class Solution:
    # BFS - O(n^2)
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        seen = set()
        mem = {}
        sentences = []        
        wordDict = set(wordDict)
        queue = [(s, "")]
        
        while queue:
            val, sent = queue.pop()

            if not val:
                sentences.append(sent)
                continue

            for word in wordDict:
                if val.startswith(word):
                    next_val = val[len(word):]
                    next_sent = (sent + " " + word).lstrip(" ")
                    if (next_val, next_sent) not in seen:
                        seen.add((next_val, next_sent))
                        queue.append((next_val, next_sent))
        
        return sentences

    # Backtracking w/ memoization - O(n^2) + optimizations
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memo):
        if s in memo: 
            return memo[s]
        
        if not s: 
            return []
        
        res = []
        for word in filter(lambda w: s.startswith(w), wordDict):                        
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest[::-1]:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
