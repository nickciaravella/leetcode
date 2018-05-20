# https://leetcode.com/problems/pascals-triangle/description/
# Easy

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        outer_list = [[1]]
        for i in range(1, numRows):
            outer_list.append([])
            for j in range(i+1):
                left =  0 if j == 0 else outer_list[i-1][j-1]
                right = 0 if j == i else outer_list[i-1][j]
                outer_list[i].append(left+right)            
        return outer_list
