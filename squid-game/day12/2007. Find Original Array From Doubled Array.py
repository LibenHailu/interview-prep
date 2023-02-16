class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        numFreq = {}
        for i in range(0, len(changed)):
            if (changed[i] in numFreq):
                numFreq[changed[i]] += 1
            else:
                numFreq[changed[i]] = 1
 
        changed.sort()
 
        res = []
 
        for i in range(0, len(changed)):
            freq = numFreq[changed[i]]
            if (freq > 0 and len(changed)) > 1 and len(changed) % 2 == 0:
                twice = 2 * changed[i]
                if twice in numFreq  and numFreq[twice] >= 1:
                    res.append(changed[i])

                    numFreq[changed[i]] -= 1
 

                    numFreq[twice] -= 1
                else:
                    return []
        return res