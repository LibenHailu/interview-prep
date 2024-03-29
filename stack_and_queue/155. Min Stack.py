class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.arr:
            self.min.append(val)    
        if self.min[-1] >= val:
            self.min.append(val)
        self.arr.append(val)
        
    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()