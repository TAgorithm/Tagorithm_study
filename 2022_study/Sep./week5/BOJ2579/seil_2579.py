# 2579 (계단오르기)
# 12:13 ~ 12:57

# dp = 각 계단의 최대치. 

n = int(input())
dp = [0] * (n+1)
dp[1] = int(input())

is_con = False
before = 0
for i in range(2, n+1):
    now = int(input())
    if is_con:
        if dp[i-3] + before + now > dp[i-2] + now:
            dp[i] = dp[i-3] + before + now
            is_con = True
        else:
            dp[i] = dp[i-2]+now
            is_con = False
    else:
        if dp[i-1]+now > dp[i-2]+now:
            dp[i] = dp[i-1]+now
            is_con = True
        else:
            dp[i] = dp[i-2]+now
            is_con = False
    before = now
print(dp[n])

# dp는 점화식을 짜는 방식이 더 좋은 것. 
# if문으로 계속 구분하면 예외가 더 생기게 된다.
# 윤현
n = int(input())
st = [0] * 300
d = [0]*300
for i in range(n):
    st[i]= int(input()) 

d[0] = st[0]
d[1] = st[0] + st[1]
d[2] = max(st[0]+st[2], st[1]+st[2])

for j in range(3,n):
    d[j] = max(d[j-2]+st[j], d[j-3]+st[j-1]+st[j])

            
print(d[n-1])


# 반례 1
# 3
# 10
# 20
# 40
# 정답: 60

# i-3까지 고려하는 것이 중요.