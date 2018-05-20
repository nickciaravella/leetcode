# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Easy

def remove_duplicates(array):
    if len(array) == 0:
        return 0

    endOfArrayIndex = 0
    for i in range(1, len(array)):
        if array[i] != array[endOfArrayIndex]:
            endOfArrayIndex += 1
            array[endOfArrayIndex] = array[i]
    return endOfArrayIndex + 1
            