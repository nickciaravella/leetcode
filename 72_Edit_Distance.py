# https://leetcode.com/problems/edit-distance/description/
# Hard

# Dynamic Programming solution
# Three choices:
#     1) Replace character (i-1, j-1) + 1
#     2) Insert character (i-1, j) + 1
#     3) Delete character (i, j-1) +1
# If they match:
#        (i-1, j-1)
# Base case:
#     empty -> * will be the len(*) - all insertions or deletions

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """        
        arr = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range(len(arr)):
            arr[i][0] = i
        for j in range(len(arr[0])):
            arr[0][j] = j
        
        for i in range(1, len(arr)):
            for j in range(1, len(arr[i])):
                if word1[i-1] == word2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:
                    arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1
                            
        # for row in arr:
        #     print(row)
        
        return arr[-1][-1]

# Example:
# "hello"
# "jelly"

# Output:
# [0, 1, 2, 3, 4, 5]
# [1, 1, 2, 3, 4, 5]
# [2, 2, 1, 2, 3, 4]
# [3, 3, 2, 1, 2, 3]
# [4, 4, 3, 2, 1, 2]
# [5, 5, 4, 3, 2, 2]

# Result:
# 2