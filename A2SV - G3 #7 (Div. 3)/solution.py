# def solve(index,profit,weight,capacity):
#     if capacity <= 0 or index >= len(profit):
#         return 0
    
#     profit1 = profit[index] + solve(index + 1,profit,weight,capacity-profit[index])
#     profit2 = solve(index + 1,profit,weight,capacity)

#     return max(profit1,profit2)

# print(solve(0,[1,6,10,16],[1,2,3,5],7))
# print(solve(0,[1,6,10,16],[1,2,3,5],6))
# def wrapper(index,profit,weight,capacity):
#     dp = [[0] * (capacity + 1) for _ in range(len(profit)) ]
#     return solve(dp,index,profit,weight,capacity)

# def solve(dp,index,profit,weight,capacity):
#     if capacity <= 0 or index >= len(profit):
#         return 0
#     if dp[index][capacity]:
#         return dp[index][capacity]

#     profit1 = profit[index] + solve(dp,index + 1,profit,weight,capacity-profit[index])
#     profit2 = solve(dp,index + 1,profit,weight,capacity)
#     dp[index][capacity] = max(profit1,profit2)
#     return dp[index][capacity]

# print(wrapper(0,[1,6,10,16],[1,2,3,5],7))
# print(wrapper(0,[1,6,10,16],[1,2,3,5],6))

def wrapper(index,profit,weight,capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(profit)) ]
    return solve(dp,index,profit,weight,capacity)

def solve(dp,index,profit,weight,capacity):
    # if capacity <= 0 or index >= len(profit):
    #     return 0
    # if dp[index][capacity]:
    #     return dp[index][capacity]

    # profit1 = profit[index] + solve(dp,index + 1,profit,weight,capacity-profit[index])
    # profit2 = solve(dp,index + 1,profit,weight,capacity)
    # dp[index][capacity] = max(profit1,profit2)
    for i in range(len(profit)):
        for c in range(1,capacity + 1):
            profit1 = profit2 = 0

            if weight[i] <= c:
                profit1 = profit[i] + dp[i - 1][c - weight[i]]

            profit2 = dp[i - 1][c]
            dp[i][c] = max(profit1,profit2)
    return dp[len(profit) - 1][capacity]

print(wrapper(0,[1,6,10,16],[1,2,3,5],7))
print(wrapper(0,[1,6,10,16],[1,2,3,5],6))