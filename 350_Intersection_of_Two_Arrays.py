# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# Easy

from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts = defaultdict(int)
        for num in nums1:
            counts[num] += 1
        
        intersection = defaultdict(int)
        for num in nums2:
            if num in counts and counts[num] > 0:
                intersection[num] += 1
                counts[num] -= 1
        
        result = []
        for num, count in intersection.items():
            result += [num] * count
        
        return result


from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1, count2 = Counter(nums1), Counter(nums2)
        return [e for e in (count1 & count2).elements()]