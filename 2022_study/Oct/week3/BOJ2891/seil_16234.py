# 인구 이동 16234
# 9:25- 10:03 (recur error)
# 10:09 (dfs->bfs로 변경해서 80% 시초)
# 10:10 pypy로 돌리니까 맞음

from collections import deque
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)#재귀 깊이 늘려줌
ans = -1 # 인구 며칠

n, l, r = map(int, input().split()) #보드크기, 몇 이상, 몇 이하

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

'''
dfs로 진행해야하고. dfs로 arr에 계속 해당 위치 추가할 것. 
추후 나중에 for문 돌면서 arr에 len만큼 나눈 값을 해당 값들로 변경해준다. 

move에는 union1, union2 ...가 존재한다
union은 [(1,2), (2,3)] 이런식으로 존재. 
'''

exit = False
visited = []
union = []
move = []
def init():
    global visited
    global move
    visited = [[0 for _ in range(n)] for _ in range(n)] # 초기화 필요.
    move = []

dy = [-1,+1,+0,+0] # 상 하 좌 우
dx = [+0,+0,-1,+1]

# def dfs(y,x):
#     global union
#     union.append((y,x)) # 자기 자신 추가.
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
        
#         if 0<=ny<n and 0<=nx<n and visited[ny][nx] == 0:
#             if l<= abs(board[y][x] - board[ny][nx]) <=r:
#                 visited[ny][nx] = -1
#                 dfs(ny,nx)

def bfs(y,x):
    global union
    qu = deque()
    qu.append((y,x))
    while qu:
        cur = qu.popleft()
        ny = cur[0]
        nx = cur[1]
        union.append((ny,nx)) # 자기 자신 추가 
        for i in range(4):
            nny = ny + dy[i]
            nnx = nx + dx[i]
            
            if 0<=nny<n and 0<=nnx<n and visited[nny][nnx] == 0:
                if l<= abs(board[ny][nx] - board[nny][nnx]) <=r:
                    visited[nny][nnx] = -1
                    qu.append((nny, nnx))
                
def pmove():
    global move
    global ans
    if move:
        for uunion in move:
            people = 0
            # uunion = [(1,2),(2,3)]
            for point in uunion:
                people += board[point[0]][point[1]]
            cpeople = people // len(uunion)
            
            for point in uunion:
                board[point[0]][point[1]] = cpeople
                
    else:
        return True

    return False
    
while not exit:
    init()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = -1
                bfs(i,j) # 이게 끝나면 union 초기화
                if len(union) != 1:
                    move.append(union) # 새로운 union 추가. (len가 1이면 자기자신만 있는 것)
                union = [] # dfs가 끝나면 union도 새로 변경
    
    exit = pmove()
    ans += 1

print(ans)


# 16234 문제 케이스
'''
dfs로 진행해야하고. dfs로 arr에 계속 해당 위치 추가할 것. 
추후 나중에 for문 돌면서 arr에 len만큼 나눈 값을 해당 값들로 변경해준다. 

move에는 union1, union2 ...가 존재한다
union은 [(1,2), (2,3)] 이런식으로 존재. 

move와 union는 다 사용하고 다시 재배열해줘야한다.
만약 더이상 이동할 인구가 없다면.(len(move) == 0 이면)
탈출하고 횟수를 return 하도록
'''

# bfs 개념
'''
# n(배열크기)가 3인 vistied 2차원배열
visited = 
[[0,0,0],
 [0,0,0],
 [0,0,0]
]

# 데이터가 있는 2차원 배열 board 
board = 
[[1,2,3],
 [4,5,6],
 [7,8,9]
]


## solve 부분
# 모든 visited를 다 돈다
# 이떄 이미 방문한 곳이면 패스한다
for y in range(n):
    for x in range(n):
        # visited 값이 0이면 방문 안 한 곳.
        # 방문 안한 곳만 방문처리하고 bfs돌리도록 
        if visited[y][x] == 0:
            visited[y][x] = -1 # 방문처리. -> 방문처리했기에 다음에 이 지점은 다시는 안 돌겠지?
            bfs(y,x)


def bfs(y,x):
    # qu를 사용해서 qu가 빌 때까지 계속 무한 루프
    # 먼저, qu에 초기값을 넣는다. 
    # 그 다음, while qu: 로 qu가 빌 때까지 계속 무한 루프를 돌린다.
    # qu에서 값을 popleft()로 값을 먼저 뺀다 (=cur)
    # 그리고 cur에서 상,하,좌,우를 고려하는데
    # 상,하,좌,우 중 조건에 맞는지 체킹한다. 
    # (이 경우 인접한 두 값을 뺀 값의 절댓값이 l과 r 사이일 때를 얘기한다)
    # 그리고 조건에 맞으면 qu에 다시 append 한다. 
    # 그리고 방문처리를 한다 -> 방문처리했기에 위 solve부분에서 -1인 값이면 pass하겠지?
    
'''