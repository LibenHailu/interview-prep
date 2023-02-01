for _ in range(int(input())):
    s = input()
    mid = len(s) // 2
    left = mid
    right = mid + 1
    left_half = []
    right_half = []
    while left >= 0 or right < len(s):
        if left >= 0:
            left_half.append(s[left])
            right_half.append(s[left])
            left -= 1
        if right < len(s):
            left_half.append(s[right])
            right_half.append(s[right])
            right += 1
    
    print("".join(reversed(left_half))+"".join(right_half))