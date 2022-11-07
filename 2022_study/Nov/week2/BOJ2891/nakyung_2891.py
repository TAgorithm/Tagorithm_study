### 카약과 강풍

import sys
input = sys.stdin.readline

# N: 팀의 수
# S: 카약이 손상된 팀의 수
# R: 카약을 하나 더 가져온 팀의 수
N, S, R = map(int, input().split())

# 카약이 손상된 팀
broken = list(map(int, input().split()))

# 카약 하나 더 가져온 팀
more = list(map(int, input().split()))

# 출발할 수 없는 팀의 수
result = len(broken)

# 자기 자신부터 먼저 없애주어야 한다
for i in broken:
    if (i in more): # 자기 자신과 같은 숫자가 more에 있으면 먼저 없애주기
        result = result - 1
        more.remove(i)
        broken.remove(i)

for i in broken:
    for j in more:
        if (i >= j-1 and i <= j+1):
            result = result - 1
            more.remove(j)

print(result)