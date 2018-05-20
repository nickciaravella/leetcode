# https://leetcode.com/problems/combinations/description/
# Medium

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        solution = []
        self.backtrack(n, k, 1, [], solution)
        return solution
    
    def backtrack(self, n, k, start, current, solution):
        if len(current) == k:
            solution.append(current[:])
        else:       
            for i in range(start, n+1):
                current.append(i)
                self.backtrack(n, k, i+1, current, solution)
                current.pop()