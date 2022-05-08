
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in ")]}":
                if stack and stack[-1] == "(" and c == ")":
                    stack.pop()
                elif stack and stack[-1] == "[" and c == "]":
                    stack.pop()
                elif stack and stack[-1] == "{" and c == "}":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
                
        return True if not stack else False