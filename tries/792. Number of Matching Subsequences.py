class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0
    
class Trie:
    def __init__(self,s):
        self.s = s
        self.root = TrieNode()
        self.ans = 0
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.count += 1
        node.end = True
    
    def find_idx(self,ch, i):
            
            for j in range(i, len(self.s)):
                if self.s[j] == ch:
                    return j
            return -1
    
    def search(self,node,last_idx):
        if node.end:
            self.ans += node.count
                
        for ch in node.children:
            idx = self.find_idx(ch, last_idx + 1)
            if idx != -1:
                self.search(node.children[ch], idx)
        return
                    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        trie = Trie(s)
        for word in words:
            trie.insert(word)
        trie.search(trie.root,-1)
        return trie.ans
         # ans = 0
        # for pre in words:
        #     ans += trie.search(pre)
        # print(ans)
        # def sub(st):
        #     pos = -1
        #     for char in st:
        #         pos = s.find(char, pos+1)
        #         if pos == -1: return False
        #     return True
        # return sum(map(sub, words))
