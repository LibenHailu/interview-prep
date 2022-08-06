
def solution(a,b):
    isYes = 'NO'
    def backtrak(a):
        nonlocal isYes
        if isYes == 'YES':
            return
        elif a == b:
            isYes = 'YES'
            return
        elif len(a) >= 2:
            newMaxA  = list(a)
            newMinA = list(a)
            newMaxA[1] = max(newMaxA[0],newMaxA[1]) 
            newMinA[1] = min(newMinA[0],newMinA[1])
            backtrak(''.join(newMaxA[1:]))
            backtrak(''.join(newMinA[1:]))   
    backtrak(a)

    return isYes

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        input2 = input()
        input3 = input()
        print(solution(input2,input3))
  