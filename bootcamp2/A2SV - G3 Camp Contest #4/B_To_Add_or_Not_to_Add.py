# use two pointers
from cgi import print_form


n,k = map(int,input().split())
nums = sorted(list(map(int,input().split())))
freq,val = 1,nums[0]
left,right = 0,1
while left < right and right < n:
    k -= (nums[right] - nums[right - 1]) * (right - left)
    if k < 0:
        k += nums[right] - nums[left]
        left += 1
    else:
        freq,val = right - left + 1,nums[right]
    right += 1 
print(f"{freq} {val}")
