# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        end_times = []
        
        intervals = sorted(intervals, key=lambda interval: interval.start)        
        for interval in intervals:
            placed = False
            for i,time in enumerate(end_times):
                if interval.start >= time:
                    placed = True
                    end_times[i] = interval.end
                    break
            if not placed:
                end_times.append(interval.end)
        
        return len(end_times)