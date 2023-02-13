from sortedcontainers import SortedDict
from collections import defaultdict

class AllOne:

    def __init__(self):
        self.word_to_count = {}
        self.count_to_words = SortedDict()
        print(self.word_to_count)

    def inc(self, key):
        if key not in self.word_to_count:
            self.word_to_count[key] = 1
            if 1 in self.count_to_words:
                self.count_to_words[1].add(key)
            else:
                self.count_to_words[1] = set()
                self.count_to_words[1].add(key)
        else:
            self.adjust_count(key, True)

    def dec(self, key):
        if key in self.word_to_count:
            self.adjust_count(key, False)

    def getMinKey(self):
        if self.count_to_words:
            data = self.count_to_words.peekitem(index=0)[1]
            return next(iter(data))
        return ""

    def getMaxKey(self):
        if self.count_to_words:
            data = self.count_to_words.peekitem()[1]
            return next(iter(data))
        return ""

    def adjust_count(self, key, isInc):
        prev_count = self.word_to_count[key]
        new_count = prev_count + 1 if isInc else prev_count - 1

        self.count_to_words[prev_count].remove(key)
        if not self.count_to_words[prev_count]:
            del self.count_to_words[prev_count]
        if new_count == 0:
                del self.word_to_count[key]
        else:
            if new_count in self.count_to_words:
                self.count_to_words[new_count].add(key)
            else:
                self.count_to_words[new_count] = set()
                self.count_to_words[new_count].add(key)
            self.word_to_count[key] = new_count 

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()/