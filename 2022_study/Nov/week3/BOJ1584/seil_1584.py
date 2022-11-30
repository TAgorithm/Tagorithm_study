# BOJ 1584 (게임)
# 0-1 BFS 문제
'''
2:23~
3:10 - 테케는 다 맞음
3:43 - 4%를 해결 못하는데 뭐가 문제일까

처음 보는 내용이다. 
'''

from collections import deque

n = int(input())
board = [[0 for _ in range(501)] for _ in range(501)]
visited = [[0 for _ in range(501)] for _ in range(501)]
### 위험
for _ in range(n):
    y1, x1, y2, x2 = map(int, input().split())
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    for i in range(miny, maxy+1):
        for j in range(minx, maxx+1):
            board[i][j] = 1

m = int(input())
### 죽음
for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    for i in range(miny, maxy+1):
        for j in range(minx, maxx+1):
            board[i][j] = -1

dy = [-1,+1,+0,+0]
dx = [+0,+0,-1,+1]

ans = 10000000
def bfs(x,y):
    global ans 
    qu = deque()
    qu.append((x,y,0))
    
    while qu:
        nx, ny, cnt = qu.popleft()
        
        if nx == 500 and ny == 500:
            ans = min(ans, cnt)
        else:
            for i in range(4):
                nny = ny + dy[i]
                nnx = nx + dx[i]
                if 0<=nny<501 and 0<=nnx<501 and visited[nny][nnx] == 0 and board[nny][nnx] != -1:
                    if cnt < ans:
                        visited[nny][nnx] = -1
                        if board[nny][nnx] == 1:
                            qu.append((nnx,nny,cnt+1))
                        else:
                            ### 이 부분이 핵심 
                            qu.appendleft((nnx,nny,cnt))
    
bfs(0,0)

if ans == 10000000:
    # 초기값 그대로면 탈출 방법 없음
    print(-1)
else:
    print(ans)
    
    


'''
문제 설명: 

죽음의구역 => 범위
위험한구역:생명-1 => 범위로 주어짐
안전한구역
(0,0) -> (500,500)

위,아래,오른쪽,왼쪽 

생명의 최솟값 +1씩 해줘야한다. 

죽음+위험=죽음 
위험+안전=위험
위험+위험=위험
죽음+안전=죽음
안전 < 위험 < 죽음 

단, 위험은 겹쳐도 생명 1씩만 감소. 

아예 못 가는 케이스도 존재 -> -1 
'''