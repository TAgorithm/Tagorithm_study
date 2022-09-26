# 계단오르기(2579) --> 맞음
n = int(input())
stair = []
dp = [0] * 301

stair.append(0)
for i in range(n):
    s = int(input())
    stair.append(s)

dp[0] = 0
dp[1] = stair[1]


if n == 1:
    pass
elif n == 2:
    dp[2] = stair[1] + stair[2]
else:
    dp[2] = stair[1] + stair[2]
    for i in range(3, n+1):

        if i == 3:
            if max(stair[1], stair[2]) == stair[2]:
                dp[i] = stair[3] + stair[2]
            elif max(stair[1], stair[2]) == stair[1]:
                dp[i] = stair[3] + stair[1]
        else:
            if stair[i-1] > stair[i-2]:
                if dp[i-3] + stair[i-1] > dp[i-2]:
                    dp[i] = dp[i-3] + stair[i] + stair[i-1]
                else:
                    dp[i] = dp[i-2] + stair[i]
                
            elif stair[i-1] < stair[i-2]:
                if dp[i-3] + stair[i-1] < dp[i-2]:
                    dp[i] = dp[i-2] + stair[i]
                else:
                    dp[i] = dp[i-3] + stair[i] + stair[i-1]

print(dp[n])

