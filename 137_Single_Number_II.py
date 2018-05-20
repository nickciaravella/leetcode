# https://leetcode.com/problems/single-number-ii/description/
# Medium

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = set()
        twice = set()
        thrice = set()

        for num in nums:
            if num in once:
                once.remove(num)
                twice.add(num)
            elif num in twice:
                twice.remove(num)
                thrice.add(num)
            else:
                once.add(num)
        
        return list(once)[0]
