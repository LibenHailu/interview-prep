class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        hash_set = set()
        needed = 0
        
        for i in range(1,len(nums) + 1):
            if nums[i - 1] in hash_set:
                duplicate = nums[i - 1]
            
            hash_set.add(nums[i - 1])
        
        for j in range(1,len(nums) + 1):
            if j not in hash_set:
                needed = j
        
        return [duplicate,needed]
        
        