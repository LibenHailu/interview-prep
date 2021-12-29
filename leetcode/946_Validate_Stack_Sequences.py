class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        deque = collections.deque(popped)
        stack = []
        for i in pushed:
            stack.append(i)
            if i == deque[0]:
                stack.pop()
                deque.popleft()
            while stack and deque and stack[-1] == deque[0]:
                stack.pop()
                deque.popleft()
         
        
        while stack and deque and stack[-1] == deque[0]:
            stack.pop()
            deque.popleft()
            
        return True if len(stack) == 0 else False