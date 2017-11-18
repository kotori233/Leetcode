class TireNode():

    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        father = self.root
        for i in word:
            child = father.children.get(i)
            if child is None:
                child = TireNode()
                father.children[i] = child
            father = child
        father.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            node = node.children.get(i)
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            node = node.children.get(i)
            if node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
