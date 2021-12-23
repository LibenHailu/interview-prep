class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                oper1 = stack.pop()
                oper2 = stack.pop()
                if i == "+":
                    stack.append(int(oper2) + int(oper1))
                elif i == "-":
                    stack.append(int(oper2) - int(oper1))
                elif i == "*":
                    stack.append(int(oper2) * int(oper1))
                elif i == "/":
                    stack.append(int(oper2) / int(oper1))
            else:
                stack.append(i)
        
        return int(stack.pop())