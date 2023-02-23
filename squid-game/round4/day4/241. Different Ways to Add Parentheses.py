class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        oprs={'-','+','*'}
        res=[]
        if expression.isdigit():
            return [int(expression)]
        for i in range(len(expression)):
            if expression[i] in oprs:
                l_ar=Solution.diffWaysToCompute(self,expression[:i])
                r_ar=Solution.diffWaysToCompute(self,expression[i+1:])
                for l in l_ar:
                    for r in r_ar:
                        if expression[i]=='*':
                            res.append(l*r)
                        elif expression[i]=='+':
                            res.append(l+r)
                        elif expression[i]=='-':
                            res.append(l-r)
        return res