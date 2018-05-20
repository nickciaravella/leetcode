# https://leetcode.com/problems/next-greater-element-i/description/
# Easy

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        starting_points = { num: i for i,num in enumerate(nums2) }
        
        result = []
        for num1 in nums1:
            added = False
            for num2 in nums2[starting_points[num1]:]:
                if num2 > num1:
                    result.append(num2)
                    added = True
                    break
            if not added:
                result.append(-1)
        return result