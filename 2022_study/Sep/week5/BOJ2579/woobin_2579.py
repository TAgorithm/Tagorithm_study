# 계단의 수
n = int(input())

# 계단에 쓰여있는 점수
scores = [0] * 300
for i in range(n):
    scores[i] = int(input())

# DP 테이블 초기화
dp = [0] * 300

# DP 진행
dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i] + scores[i-1])

print(dp[n-1])