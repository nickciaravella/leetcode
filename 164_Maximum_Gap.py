import math

# Bucket sort + pigeon hole principle
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return max(nums)-min(nums)
        
        min_val, max_val = min(nums), max(nums)     
        # want n-1 buckets (n-2 elements since we can exclude min and max)
        # size of each bucket is max-min / #buckets, round up to make easier to compute with
        bucket_count = len(nums)-1
        bucket_size = math.ceil((max_val-min_val) / bucket_count)
        buckets_min = [2**33] * bucket_count
        buckets_max = [-1] * bucket_count
        
        # put in buckets
        for num in nums:
            if num == min_val or num == max_val:
                continue
            bucket = (num-min_val) // bucket_size
            buckets_min[bucket] = min(buckets_min[bucket], num)
            buckets_max[bucket] = max(buckets_max[bucket], num)
        
        prev = min_val
        max_distance = -1
        # Find the max distance between buckets
        # note, at least one will be empty so the min/max should cross an empty bucket
        # min -> [] -> [] -> [] -> max
        for i in range(bucket_count):
            if buckets_min[i] == 2**33: continue
            max_distance = max(buckets_min[i] - prev, max_distance)
            prev = buckets_max[i]
        max_distance = max(max_val - prev, max_distance)
            
        return max_distance