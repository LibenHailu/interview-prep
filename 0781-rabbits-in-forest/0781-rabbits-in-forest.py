class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        print(count)
        ans = 0
        for key,value in count.items():
             ans+=(key+1)*ceil(value/(key+1))
        return ans
            