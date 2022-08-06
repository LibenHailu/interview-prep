def solution(height,friends):
    res = 0
    for friend in friends:
        if friend > height:
            res += 2
        else:
            res += 1
    
    return res

if __name__ == '__main__':
    
    input1 = list(map(int, input().rstrip().split()))
    input2 = list(map(int, input().rstrip().split()))
    print(solution(input1[1],input2))

