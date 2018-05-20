# https://leetcode.com/problems/task-scheduler/description/
# Medium

from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        heap = [-count for _, count in Counter(tasks).items()]
        heapq.heapify(heap)

        iteration_count = 0
        while heap:
            
            topush = []
            for i in range(n+1):
                if heap:
                    val = heapq.heappop(heap)
                    topush.append(val+1)
            
            for val in topush:
                if val != 0:
                    heapq.heappush(heap, val)
            
            if heap:
                iteration_count += n + 1
            else:
                iteration_count += len(topush) 

        return iteration_count

s = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(s.leastInterval(tasks, n))
