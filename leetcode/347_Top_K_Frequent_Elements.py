class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        nums.sort()
        out = []
        for i in nums:
            if i in freq:
                freq[i]+= 1
            else:
                freq[i] = 1
        
        freq = sorted(freq.items() ,key=lambda x : x[1],reverse=True)
        
        count = 0
        for i in  freq:
            if count < k:
                out.append(i[0])
                count+=1
            else:
                break
        
        return out

        
        
        