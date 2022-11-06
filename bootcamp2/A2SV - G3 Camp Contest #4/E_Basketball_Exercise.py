n = int(input())
team1 = list(map(int,input().split()))
team2 = list(map(int,input().split()))
dp = [0,0]
for i in range(n):
    x = max(dp[0], dp[1] + team1[i] )
    y = max(dp[1], dp[0] + team2[i] )
    dp[0],dp[1] = x,y

print(max(dp))

