class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        memo = {}

        for word in words:
            memo[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in memo:
                    memo[word] = max(memo[word], 1 + memo[predecessor])
        return max(memo.values())
     