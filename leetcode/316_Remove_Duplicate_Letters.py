class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        c = Counter(s)
        inStack = set()

        for char in s:
            if char in stack:
                c[char] -= 1

            else:
                while stack and stack[-1] > char and c[stack[-1]] >= 1:
                    poped = stack.pop()
                    inStack.remove(poped)
                stack.append(char)
                c[stack[-1]] -= 1
                inStack.add(char)
        return "".join(stack)
