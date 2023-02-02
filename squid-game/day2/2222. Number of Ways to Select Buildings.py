class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix=[0] 
        suffix = [0]
        for i in s:
            if i == '1':
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        
        for i in reversed(s):
            if i == '1':
                suffix.append(suffix[-1] + 1)
            else:
                suffix.append(suffix[-1])
        suffix = suffix[::-1]
        ans = 0
        for index,val in enumerate(s):
            
            if val == '0':
                ans += prefix[index] * suffix[index]
            else:
                ans += (index - prefix[index]) * (len(s) - index - suffix[index] )
        return ans

            

            
