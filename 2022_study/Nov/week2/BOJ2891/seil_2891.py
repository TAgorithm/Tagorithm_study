# 카약과 강풍
'''
# 풀이1: bfs
# 풀이2: dfs 
'''

# 풀이1: bfs (6:20~7:32)

from collections import deque
n, s, r= map(int, input().split()) # 팀수, 카약손상팀수, 더들고온팀수
team = [0] * n
for bidx in list(map(int, input().split())):
    team[bidx-1] = -1

more = [0] * n
for midx in list(map(int, input().split())):
    more[midx-1] = 1

ans = 100

dx = [0,-1,1] # 나 자신, 왼쪽, 오른쪽
def bfs(team, more):
    global ans
    qu = deque()
    qu.append([team, more])
    while qu:
        cur = qu.popleft()
        nteam = cur[0]
        nmore = cur[1]
        
        # 탈출: 더이상 카약이 없을 때 
        if sum(nmore) == 0:
            ans = min(ans, abs(sum(nteam)))
        else:
            is_fin = True
            for i in range(len(nmore)):
                if nmore[i] == 1:
                    for j in range(3):
                        nx = i+dx[j]
                        if j == 0 and 0<=nx<n and nteam[nx] == -1:
                            # 자기 자신이면 자기만 주고 break
                            is_fin = False
                            nteam[nx] = 0
                            nmore[i] = 0
                            qu.append([nteam[:], nmore[:]])
                            nteam[nx] = -1
                            nmore[i] = 1
                            break
                        # 자신이 여분이 있는 사람에게는 빌려주면 안된다.
                        elif 0<=nx<n and nteam[nx] == -1:
                            if team[nx] == -1 and more[nx] == 1:
                                continue
                            is_fin = False
                            nteam[nx] = 0
                            nmore[i] = 0
                            qu.append([nteam[:], nmore[:]])
                            nteam[nx] = -1
                            nmore[i] = 1
        
        if is_fin:
            ans = min(ans, abs(sum(nteam)))
                        
bfs(team, more)
print(ans)


# 풀이2: dfs (11:44 ~ 12:10)

n, s, r = map(int, input().split())
team = [0] * n
more = [0] * n
for i in map(int, input().split()):
    team[i-1] = -1 

for i in map(int, input().split()):
    more[i-1] = 1


dx = [-1, +1]
ans = abs(sum(team))
def dfs(Nteam, Nmore):
    global ans
    if sum(Nmore) == 0:
        # 더이상 치유할 수 없는 상태면 계산 x
        ans = min(ans, abs(sum(Nteam)))
        return 
    if sum(Nteam) == 0:
        # 모든 팀이 치유될 때는 더이상 계산 x
        ans = 0
        return
    for i in range(len(Nmore)):
        if Nmore[i] == 1:
            if Nteam[i] == -1:
                # 자기 자신 고치기
                Nmore[i] = 0
                Nteam[i] = 0
                ans = min(ans, abs(sum(Nteam))) # 이걸 매번 해야할까.
                dfs(Nteam[:], Nmore[:])
            else:
                for j in range(2):
                    nx = i + dx[j]
                    if 0<=nx<n and Nteam[nx] == -1:
                        Nteam[nx] = 0
                        Nmore[i] = 0
                        ans = min(ans, abs(sum(Nteam))) # 이걸 매번 해야할까.
                        dfs(Nteam[:], Nmore[:])
                        # 원상복귀
                        Nteam[nx] = -1
                        Nmore[i] = 1
            
        
dfs(team, more)
print(ans)


### 반례
# 10 5 2
# 1 2 3 6 7            
# 7 8
# 정답: 4

# 10 1 1
# 1
# 3
# 정답: 1

# 10 5 2
# 1 2 3 6 7            
# 7 8
# 정답: 4


'''
풀이 생각 과정

3번 팀 4,5만 빌려주기 가능
일부팀만 더 카약 존재. 
자신이 broken은 자기 자신 먼저 줄 것.

# 최소값: dp 혹은 탐욕 혹은 완탐(dfs)
'''