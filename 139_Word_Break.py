# https://leetcode.com/problems/word-break/description/
# Medium

class Solution:

    # DFS
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        stack = [s]
        seen = {s}

        while stack:
            word = stack.pop()
            if not word:
                return True

            for next_word in [word[len(e):] for e in wordDict if word.startswith(e)]:
                if next_word not in seen:
                    seen.add(next_word)
                    stack.append(next_word)
        
        return False

    # DP
    def wordBreakDp(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if (i == 0 or dp[i-1] == True) and s[i:j+1] in wordDict:
                    dp[j] = True

        return dp[-2]
