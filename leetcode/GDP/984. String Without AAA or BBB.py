class Solution(object):
    def strWithout3a3b(self, A, B):
        ans = []
        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B
            
            if writeA:
                ans.append('a')
                A -= 1
            else:
                ans.append('b')
                B -= 1
        
        return "".join(ans)
                
        