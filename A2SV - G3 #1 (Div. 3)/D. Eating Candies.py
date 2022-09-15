def solution(candies):
    if len(candies) == 1:
        return 0
    # set two pointers
    # accumulate left and right sums
    # if both sums are equal shift your both pointers
    # if one is smaller shit along that dir
    # save your best when both sums are  equal
    left = 0
    right =  len(candies) - 1
    leftSum = candies[0]
    rightSum =  candies[len(candies) - 1]
    res = 0
    while left < right and 0 <= left < len(candies) and 0 <= right < len(candies):
        if leftSum < rightSum:
            left += 1
            leftSum += candies[left]
        elif rightSum < leftSum:
            right -= 1
            rightSum += candies[right]
        # elif left == 0:
        #     leftSum += candies[0]
        # elif right == len(candies) - 1:
        #     rightSum += candies[len(candies) - 1]
        elif rightSum == leftSum:
            res = (left + 1) + (len(candies) - right)
            left += 1
            right -= 1
            leftSum += candies[left]
            rightSum += candies[right]
    return res

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        print(solution(list(map(int, input().split()))))

    