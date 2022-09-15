def solution(nums):
    # 2412
    # 4 is bad index
    # set = 4
    # set = 4 2
    # bad = set()
    bad = None
    hashSet = set()
    for i in range(1,len(nums)):
        if nums[i] < nums[i - 1]:
            bad = i -  1
        # if bad and nums[bad] == nums[i]:
        #     bad = i
    
    for i in range(len(nums)):
        if i <= bad:
            hashSet.add(nums[i])
        elif nums[i] in hashSet:
            bad = i
            
    print(set(nums[:bad+1]),bad)
    return len(set(nums[:bad+1])) if bad else 0
        # if nums[i - 1] > nums[i]:
        #     bad.add(nums[i-1])
        #     nums[i-1] = 0
        #     cur_index = i-1
        #     while cur_index >= 1:
        #         if nums[cur_index - 1] > nums[cur_index]:
        #             bad.add(nums[cur_index-1])
        #             nums[cur_index-1] = 0
        #         cur_index -= 1
    # return len(bad)


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        print(solution(list(map(int, input().split()))))