for _ in range(int(input())):
    n = int(input())
    s1 = list(input())
    s2 = list(input())
    ans = 0
    visited = set()
    visited_s2 = set()
    for i in range(len(s2)):
        if s2[i] == '0':
            continue
        if i - 1 >= 0 and s1[i - 1] == '1' and (i - 1) not in visited and i not in visited_s2:
            visited.add(i - 1)
            visited_s2.add(i)
            ans += 1
        if s1[i] == '0' and i not in visited and i not in visited_s2:
            visited.add(i)
            visited_s2.add(i)
            ans += 1
        if i + 1 < len(s1) and s1[i + 1] == '1' and i + 1 not in visited and i not in visited_s2:
            visited.add(i + 1)
            visited_s2.add(i)
            ans += 1

        # print(visited)
        # print(ans)
    print(ans)




    