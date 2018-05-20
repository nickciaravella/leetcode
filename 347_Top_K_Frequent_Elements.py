# https://leetcode.com/problems/top-k-frequent-elements/description/
# Medium

from collections import Counter

# Using Counter (cheating)
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter(nums)
        return list(map(lambda x: x[0], cnt.most_common(k)))

# Using bucket sort
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # get counts for each element: O(n)
        cnt_per_el = {}
        for num in nums:
            if num in cnt_per_el:
                cnt_per_el[num] += 1
            else:
                cnt_per_el[num] = 1
           
        # put elements into buckets based on their count: O(n)
        buckets = [0] * (len(nums)+1)
        for num, cnt in cnt_per_el.items():
            if not buckets[cnt]:
                buckets[cnt] = [num]
            else:
                buckets[cnt].append(num)
        
        # construct result: O(n)
        ret = []
        i = len(buckets)-1
        while len(ret) < k and i >= 0:
            if buckets[i]:
                ret.append(buckets[i].pop())
            else:
                i-=1
                
        return ret