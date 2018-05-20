# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# Easy

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left_vowel = 0
        right_vowel = len(s)-1
        while left_vowel < right_vowel:
            if s[left_vowel].lower() not in vowels:
                left_vowel += 1
            if s[right_vowel].lower() not in vowels:
                right_vowel -= 1
            if s[left_vowel].lower() in vowels and s[right_vowel].lower() in vowels:
                s[left_vowel], s[right_vowel] = s[right_vowel], s[left_vowel]
                left_vowel += 1
                right_vowel -= 1
        return ''.join(s)