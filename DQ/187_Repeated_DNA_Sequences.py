class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mySet = set()

        result = set()
        for i in range(len(s)):
            if i+10 - i == 10 and i+10 <= len(s):
                if not s[i:i+10] in mySet:
                    mySet.add(s[i:i+10])

                else:
                    result.add(s[i:i+10])

        return result
