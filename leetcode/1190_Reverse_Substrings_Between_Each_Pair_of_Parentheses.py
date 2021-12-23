class Solution:
    def reverseParentheses(self, s: str) -> str:
        s1 = []
        for c in s:
            if c == ")" and s1:
                print("yeah")
                s2 = []
                s3 = []
                while s1[-1] != "(": 
                    s2.append(s1.pop())
                
                s1.pop()

                while s2:
                    s3.append(s2.pop())
                
                while s3:
                    s1.append(s3.pop())
                
                print(s1)
                                    
            else:
                s1.append(c)
          
        return "".join(s1)
