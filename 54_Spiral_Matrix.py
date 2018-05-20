# https://leetcode.com/problems/spiral-matrix/description/
# Medium

class Solution(object):
    def printmatrix(self, matrix):
        print("------------")
        for r in matrix:
            print(r)
            
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """                
        ret = []
        if not matrix:
            return ret
        
        offset = 0
        rows = len(matrix)
        columns = len(matrix[0])
        while rows-offset > offset and columns-offset > offset:
            
            # go right
            for i in range(offset, columns-offset):
                if matrix[offset][i] is not None:
                    ret.append(matrix[offset][i])
                    matrix[offset][i] = None
            #self.printmatrix(matrix)
            
            # go down
            for i in range(offset, rows-offset):
                if matrix[i][columns-offset-1] is not None:
                    ret.append(matrix[i][columns-offset-1])
                    matrix[i][columns-offset-1] = None
            #self.printmatrix(matrix)
            
            # go left
            for i in range(offset, columns-offset):
                if matrix[rows-offset-1][columns-i-1] is not None:
                    ret.append(matrix[rows-offset-1][columns-i-1])
                    matrix[rows-offset-1][columns-i-1] = None
            #self.printmatrix(matrix)
            
            # go up
            for i in range(offset, rows-offset):
                if matrix[rows-i-1][offset] is not None:
                    ret.append(matrix[rows-i-1][offset])
                    matrix[rows-i-1][offset] = None
            #self.printmatrix(matrix)
            
            offset+=1
            
        return ret