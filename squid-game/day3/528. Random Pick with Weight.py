class Solution:

    def __init__(self, w: List[int]):
        self.prefix =  []
        for num in w:
            if not self.prefix:
                self.prefix.append(num)
            else:
                self.prefix.append(num + self.prefix[-1])       

    def pickIndex(self) -> int:
        rand = random.randint(0, len(self.prefix)) 
        return bisect_left(self.prefix, rand)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()