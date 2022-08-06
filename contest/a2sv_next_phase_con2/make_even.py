
import sys



def solution(num):
    def isEven(n):
        return n % 2 == 0
    def swap(num,l):
        n = num
        left,right = 0 , l
        while left < right and left >= 0 and right < len(n):
            n[left],n[right] = n[right],n[left]
            left += 1
            right -= 1
        
        return n

    if len(num) == 1:
        if isEven(int(num)):
            return int(num)
        else:
            return -1
    
    minSwap = sys.maxsize
    if isEven(int(num)):
        return 0
    else:
        for i in range(1,len(num)):
            l = i
            start = i
            n = num
            while l < len(num):
                swapped = swap(list(n),l)
                if isEven(int(''.join(swapped))):
                    minSwap = min(minSwap,l - start + 1) 
                    break
                n = ''.join(swapped)
                l += 1
    return minSwap if minSwap != sys.maxsize else -1
    
    

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        print(solution(input()))