# 11:44 ~ 12:10

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


# 10 1 1
# 1
# 3
# 정답: 1

# 10 5 2
# 1 2 3 6 7            
# 7 8
# 정답: 4

