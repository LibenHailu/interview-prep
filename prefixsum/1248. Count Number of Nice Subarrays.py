class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref=list(accumulate([0 if num%2==0 else 1 for num in nums]))
        d  = {0:1}
        ans = 0
        for num in  pref:
            if num - k in d:
                ans += d[num - k]
            d[num] = 1 + d.get(num,0)
        return ans
        # dico=defaultdict(int)
        # res=0
        # dico[0]=1
        # for num in pref:
        #     if num-k in dico:
        #         res+=dico[num-k]
        #     dico[num]+=1
        # return res