# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Medium

# Not the best solution, better to have an "isWord" field on trie-node to
# make search and startsWith more consistent. Also, can use default dict and
# no need to store the value of each TrieNode since the dictionary has it.

class TrieNode:
    
    def __init__(self, val):
        self.val = val
        self.children = {}

class Trie:
                
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
        self.allWords = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.allWords.add(word)
        self.insert_helper(word, self.root)
        
    def insert_helper(self, word, root):
        if not word:
            return
        
        letter = word[0]
        if letter not in root.children:            
            root.children[letter] = TrieNode(letter)
            
        self.insert_helper(word[1:], root.children[letter])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.allWords                

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        word = prefix
        while word:
            if word[0] not in cur.children:
                return False
            cur = cur.children[word[0]]
            word = word[1:]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)