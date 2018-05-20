# https://leetcode.com/problems/group-anagrams/description/
# Medium

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for val in strs:            
            sortedVal = ''.join(sorted(val))            
            if sortedVal in groups:
                groups[sortedVal].append(val)
            else:
                groups[sortedVal] = [val]
            
        return list(groups.values())

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))