class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root

        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                current.children[index] = Node()
            current = current.children[index]
        current.isEnd = True

    def search(self, word, isPrefix=False):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current.isEnd or isPrefix:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return self.search(prefix, True)


class Node():
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
