# https://leetcode.com/submissions/detail/146587194/
# Hard

from collections import defaultdict

class Graph:

    def __init__(self):
        
        # {
        #   "vertex": { set of vertices }
        # }
        self.adjmap = defaultdict(set)

    def addEdge(self, start, end):
        self.adjmap[start].add(end)

    def addVertex(self, vertex):
        if vertex not in self.adjmap:
            self.adjmap[vertex] = set()

    # Topological sort:
    # https://www.geeksforgeeks.org/topological-sorting/ 
    # Orders all of the least dependent vertices before the
    # most dependent.
    def topologicalSort(self):        
        sortedList = []
        visited = set()    
        for vertex in self.adjmap:
            if vertex not in visited:            
                if not self.topologicalSortFrom(vertex, visited, set(), sortedList):
                    return []
                
        return sortedList[::-1]

    # Does a topological sort from a starting vertex. If it detects
    # a cycle, it will return False
    def topologicalSortFrom(self, startVertex, visited, visiting, outputList):
        if startVertex in visiting:
            return False
        
        visiting.add(startVertex)

        if startVertex in self.adjmap:        
            for vertex in self.adjmap[startVertex]:
                if vertex not in visited:
                    if not self.topologicalSortFrom(vertex, visited, visiting, outputList):
                        return False
        
        visiting.remove(startVertex)
        visited.add(startVertex)
        outputList.append(startVertex)

        return True

    def view(self):
        for key, val in self.adjmap.items():
            print(key, list(val))

class Solution:

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = Graph()

        # Create a vertex for every letter
        # This is needed to include letters that have
        # no edges.
        for letter in (char for word in words for char in word):
            graph.addVertex(letter)

        # Create edges by finding the first different
        # character in each adjacent word.
        for word1, word2 in zip(words, words[1:]):        
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    graph.addEdge(letter1, letter2)
                    break
        
        #graph.view()
        
        # Do a topological sort to create the letter ordering
        return ''.join(graph.topologicalSort())

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
# words = [
#     'z', 
#     'z' 
# ]
# words = [
#     'a', 
#     'b',
#     'a' 
# ]
s = Solution()
order = s.alienOrder(words)
print(order)