class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        current = self.root
        
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.freq += 1
    
    def counter(self):
        def find_count(node,s):
            if node.freq > 0:
                lst.append((-node.freq,s))
            for char in node.children:
                find_count(node.children[char], s+char)
        lst = []
        find_count(self.root, '')
        
        return lst
                
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        heap = trie.counter()
        heapq.heapify(heap)
        res = []
        while heap and k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res