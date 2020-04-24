#problem 208 / implement trie
# Trie / prefix tree / dictonary
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        t = self.trie
        for let in word:
            if let not in t:
                t[let] = {}
            t = t[let]
        t['#'] = '#'
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for let in word:
            if let not in t:
                return False
            t = t[let]
        if '#' in t:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for let in prefix:
            if let not in t:
                return False
            t = t[let]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)