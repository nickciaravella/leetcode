# https://leetcode.com/problems/design-search-autocomplete-system/description/
# Hard

import heapq

class RankedPredictions:

    # def __init__(self):
    #     self.sentence_count = {}        

    # # O(1) - writes will be fast
    # def updatePrediction(self, sentence, times):
    #     if sentence in self.sentence_count:
    #         self.sentence_count[sentence] -= times
    #     else:
    #         self.sentence_count[sentence] = -times

    # # O(nlgn) - reads will be slow
    # def getTopThree(self):
    #     heap = [(count, sentence) for sentence, count in self.sentence_count.items()]
    #     heapq.heapify(heap)
    #     return [sentence for _, sentence in heapq.nsmallest(3, heap)]

    def __init__(self):
        self.sentence_count = []

    # O(nlgn) - keep it sorted (writes will be slow)
    def updatePrediction(self, sentence, times):
        found = False
        for i in range(len(self.sentence_count)):
            count, cur_sentence = self.sentence_count[i]
            if cur_sentence == sentence:
                self.sentence_count[i] = (count-times, sentence)
                found = True
                break

        if not found:
            self.sentence_count.append((-times, sentence))

        heapq.heapify(self.sentence_count)        

    # O(1) - reads will be fast
    def getTopThree(self):
        return [sentence for count, sentence in heapq.nsmallest(3, self.sentence_count)]

class TrieNode:

    def __init__(self):
        self.children = {}
        self.predictions = RankedPredictions()

    def goTo(self, char):
        if char in self.children:
            return self.children[char]
        else:
            raise ValueException("No child '" + char + "'")
    
    def has(self, char):
        return char in self.children

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence, times):
        self.insert_helper(sentence, times, sentence, self.root)

    def insert_helper(self, sentence, times, toInsert, curNode):
        curNode.predictions.updatePrediction(sentence, times)

        if not toInsert:
            return

        char = toInsert[0]        
        if char not in curNode.children:
            curNode.children[char] = TrieNode()
        
        self.insert_helper(sentence, times, toInsert[1:], curNode.children[char])        


class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """    
        self.trie = Trie()
        for sentence, rank in zip(sentences, times):
            self.trie.insert(sentence, rank)

        self.curNode = self.trie.root
        self.curWord = ""

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.trie.insert(self.curWord, 1)
            self.curNode = self.trie.root
            self.curWord = ""
            return []

        if self.curNode and self.curNode.has(c):
            self.curNode = self.curNode.goTo(c)
        else:
            self.curNode = None

        self.curWord += c
        
        if self.curNode:
            return self.curNode.predictions.getTopThree()
        else:
            return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

sentences = [
    "i love you",
    "island",
    "ironman",
    "i love leetcode"
]
times = [
    5,
    3,
    2,
    2
]

acs = AutocompleteSystem(sentences, times)
chars = list("i hate you")
for i in range(10):
    for char in chars:
        print(char, acs.input(char))
    acs.input('#')
