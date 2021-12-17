
"""
https://leetcode.com/problems/sorting-the-sentence/
"""
class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i][-1] > arr[j][-1]:
                    arr[i],arr[j] = arr[j],arr[i]
        
        return " ".join(map(lambda x: x[:-1],arr))
        