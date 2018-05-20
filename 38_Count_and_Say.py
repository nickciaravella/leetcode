# https://leetcode.com/problems/count-and-say/description/
# Easy

def get_next(seq):
    nextSeq = ""
    currentChar = seq[0]
    currentCount = 1
    for i in range(1, len(seq)):        
        char = seq[i]
        if char == currentChar:
            currentCount += 1
        else:
            nextSeq += str(currentCount) + currentChar
            currentCount = 1
            currentChar = char
    nextSeq += str(currentCount) + currentChar
    return nextSeq


def count_and_say(n):
    if n == 0:
        return ""
    if n == 1: 
        return "1"

    i = 2
    seq = "1"
    while i <= n:
        seq = get_next(seq)
        i += 1
    return seq
