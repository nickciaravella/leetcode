# https://leetcode.com/problems/word-pattern-ii/description/
# Hard

class Solution:
    def wordPatternMatch(self, pattern, word):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.backtrack(pattern, word, {}, set())
        
    def backtrack(self, pattern, word, mapping, used):
        
        #print("pattern: " + pattern)
        #print("   word: " + word)
        #print("mapping: " + str(mapping))
        #print("------------------------")
        
        if not word and not pattern:
            return True
        if not word or not pattern:
            return False

        pattern_letter = pattern[0]
        if pattern_letter in mapping:
            if not word.startswith(mapping[pattern_letter]):
                return False
            else:
                return self.backtrack(pattern[1:], word[len(mapping[pattern_letter]):], mapping, used)

        for i in range(1, len(word)+1):
            candidate = word[:i]
            if candidate not in used:
                mapping[pattern_letter] = candidate
                used.add(candidate)

                if self.backtrack(pattern[1:], word[i:], mapping, used):
                    return True

                del mapping[pattern_letter]
                used.remove(candidate)

        return False

# Sample Input:
# "abab"
# "redblueredblue"

# Sample Return Value:
# True

# Sample Output:
# pattern: abab
#    word: redblueredblue
# mapping: {}
# ------------------------
# pattern: bab
#    word: edblueredblue
# mapping: {'a': 'r'}
# ------------------------
# pattern: ab
#    word: dblueredblue
# mapping: {'b': 'e', 'a': 'r'}
# ------------------------
# pattern: ab
#    word: blueredblue
# mapping: {'b': 'ed', 'a': 'r'}
# ------------------------
# pattern: ab
#    word: lueredblue
# mapping: {'b': 'edb', 'a': 'r'}
# ------------------------
# pattern: ab
#    word: ueredblue
# mapping: {'b': 'edbl', 'a': 'r'}
# ------------------------
# pattern: ab
#    word: eredblue
# mapping: {'b': 'edblu', 'a': 'r'}
# ------------------------
# pattern: ab
#    word: redblue
# mapping: {'b': 'edblue', 'a': 'r'}
# ------------------------
# pattern: b
#    word: edblue
# mapping: {'b': 'edblue', 'a': 'r'}
# ------------------------
# pattern: 
#    word: 
# mapping: {'b': 'edblue', 'a': 'r'}
# ------------------------
