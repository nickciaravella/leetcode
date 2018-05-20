# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
# Medium

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_eow = False
    
    def get_all_children(self):
        return self.children.values()

    def get_child(self, letter):
        if letter in self.children:
            return self.children[letter]
        else:
            return None

    def add_child(self, letter, node):
        self.children[letter] = node

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            child = current.get_child(letter)
            if child is None:
                child = TrieNode()
                current.add_child(letter, child)
            current = child
        current.is_eow = True            
            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_helper(word, 0, self.root)

    def search_helper(self, word, index, node):
        if index == len(word):
            return node.is_eow
        
        if word[index] == '.':
            return any([self.search_helper(word, index+1, n) for n in node.get_all_children()])

        child = node.get_child(word[index])
        if child is None:
            return False
        
        return self.search_helper(word, index+1, child)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

def Test(word, search_word, expected):
    s = WordDictionary()
    s.addWord(word)
    print(s.search(search_word), expected)

Test("hello", "hello", True)
Test("hello2", "hello", False)
Test("hello", "hello2", False)
Test("hello", "h...o", True)
Test("hello", "h.", False)
Test("", "", True)
Test("", ".", False)
Test(".", ".", True)
