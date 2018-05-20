# https://leetcode.com/problems/merge-intervals/description/
# Medium

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        new_intervals = [sorted_intervals[0]]

        for interval in sorted_intervals[1:]:
            if interval.start <= new_intervals[-1].end:
                new_intervals[-1].end = max(new_intervals[-1].end, interval.end)
            else:
                new_intervals.append(interval)
        return new_intervals

s = Solution()
vals = s.merge([Interval(15, 18), Interval(2, 6), Interval(8, 10), Interval(1, 3)])
for v in vals:
    print(f'[{v.start}, {v.end}]')