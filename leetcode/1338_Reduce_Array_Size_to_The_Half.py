class Solution:
    def minSetSize(self, arr: List[int]) -> int:
            n = len(arr)
            freq_map = {}
            for i in arr:
                if i in freq_map:
                    freq_map[i] += 1
                else:
                    freq_map[i] = 1
            freq_map = sorted(freq_map.items(), key=lambda x:x[1], reverse=True)
            num = 0
            for i in freq_map:
                n -= i[1]
                num += 1 
                if n * 2 <= len(arr):
                    break
            return num
