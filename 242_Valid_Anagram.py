# https://leetcode.com/problems/valid-anagram/description/
# Easy

# Works for any number of characters
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}
        for letter_s, letter_t in zip(s, t):
            hash_s[letter_s] = 1 if letter_s not in hash_s else hash_s[letter_s] + 1
            hash_t[letter_t] = 1 if letter_t not in hash_t else hash_t[letter_t] + 1
        
        hashes_s = { (key, value) for key, value in hash_s.items() }
        hashes_t = { (key, value) for key, value in hash_t.items() }

        return (hashes_s - hashes_t) == set()

# Works for only lowercase ASCII characters
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        letter_counts = [0 for i in range(26)]
        for letter_s, letter_t in zip(s,t):
            letter_counts[ord(letter_s)-ord('a')] += 1
            letter_counts[ord(letter_t)-ord('a')] -= 1
        return all(c == 0 for c in letter_counts)
