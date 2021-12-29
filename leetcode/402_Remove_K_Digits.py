class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i,n in enumerate(num):
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
                
            if len(stack)==1 and stack[-1] == '0': 
                stack.pop()
                
            stack.append(n)
        
        while stack and k:
            stack.pop()
            k -= 1
        

        return ''.join(stack) or '0'