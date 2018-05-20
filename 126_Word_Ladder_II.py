import collections
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """                            
        tree, path, paths = collections.defaultdict(list), [beginWord], []
        is_found = self.bfs_level(set([beginWord]), set([endWord]), tree, True, set(wordList))
        print(tree)
        return self.construct_paths(beginWord, endWord, tree)

    def bfs_level(self, current, reverse, tree, direction, words_set):
        
        # If we hit an empty list, then there is no solution
        if not current: 
            return False

        # Always process the smaller of the BFS
        if len(current) > len(reverse):
            return self.bfs_level(reverse, current, tree, not direction, words_set)

        # Remove all words already found from the set so we don't
        # have cycles. We already found the shortest path to each of them.
        for word in (current | reverse):
            words_set.discard(word)

        next_lev, done = set(), False
        while current:
            word = current.pop()
            for c in string.ascii_lowercase:
                for index in range(len(word)):
                    candidate = word[:index] + c + word[index+1:]
                    
                    # The word is already found in the opposite search
                    # so the searches have merged and we are done.
                    if candidate in reverse:
                        done = True
                        self.add_path(tree, word, candidate, direction)        

                    if not done and candidate in words_set:
                        next_lev.add(candidate)
                        self.add_path(tree, word, candidate, direction)

        return done or self.bfs_level(next_lev, reverse, tree, direction, words_set)

    def add_path(self, tree, word, candidate, direction):
        if direction: 
            tree[word] += candidate,
        else:       
            tree[candidate] += word,

    def construct_paths(self, source, dest, tree):
        if source == dest: 
            return [[source]]
        return [[source] + path for succ in tree[source]
                                for path in self.construct_paths(succ, dest, tree)]


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
s = Solution()
print(s.findLadders(beginWord, endWord, wordList))
