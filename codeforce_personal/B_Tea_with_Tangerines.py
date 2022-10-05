for s in[*open(0)][2::2]:
    a=*map(int,s.split()),;
    # print(a)
    m=2*min(a)-1;
    # print([-x//m+1 for x in a])
    print(-sum(-x//m+1 for x in a))