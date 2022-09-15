# for each test case
# accept the two lines of color pixels
# add them to set
# check len print the res
tc = int(input())
for _ in range(tc):
    hashSet = set()
    hashSet = hashSet.union(set(list(input())))
    hashSet = hashSet.union(set(list(input())))
    if len(hashSet) == 1:
        print(0)
    elif len(hashSet) == 2:
        print(1)
    elif len(hashSet) == 3:
        print(2)
    else:
        print(3)