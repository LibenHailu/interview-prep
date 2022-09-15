def solution(n,p,q):
    # create a set of size n
    # merge both levels to one list
    # make it a set
    # compare two sets
    # print the output
    levels = set([i for i in range(1,n+1)])
    p.extend(q)
    capacity = set(p)
    return levels == capacity

if __name__ == "__main__":
    n = int(input())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    res = solution(n,p[1:],q[1:])
    if res:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
    