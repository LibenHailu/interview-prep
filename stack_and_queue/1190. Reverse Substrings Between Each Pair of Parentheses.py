class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = []
        
        for c in s:
            if c == ")":
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                
                stack.pop()
                stack.extend(temp)
                temp = []
            
            else:
                stack.append(c)
        
        return "".join(stack)