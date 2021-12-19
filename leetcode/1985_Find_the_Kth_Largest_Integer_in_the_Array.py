class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = sorted(list(map(int,nums)),reverse=True)
        return str(num[k-1])
