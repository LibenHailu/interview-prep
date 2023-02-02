class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            if num != 0:
                hash_set.add(num)
        return len(hash_set)