# https://leetcode.com/problems/flatten-nested-list-iterator/description/
# Medium

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flattenedList = []
        for nested in nestedList:
            self.flatten(nested)
        self.i = 0
        
    def next(self):
        """
        :rtype: int
        """
        val = self.flattenedList[self.i]
        self.i += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.flattenedList)
        
    def flatten(self, nestedList):
        if nestedList.isInteger():
            self.flattenedList.append(nestedList.getInteger())            
        else:
            for nested in nestedList.getList():
                if nested.isInteger():
                    self.flattenedList.append(nested.getInteger())
                else:
                    self.flatten(nested)
            
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())