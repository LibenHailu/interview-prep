from tkinter import N


def solution(nums):
    if len(nums) == 1:
        return 0
    hashSet = set()
    for i in range(len(nums)-1):
        
        hashSet.add(nums[i])
    return len(hashSet)
