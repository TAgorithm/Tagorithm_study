# 학부 연구생 민상(21922)
# 6:44-7:48 (O)

'''
visited면 cnt + 1 x
9면 bfs돌 것. 1,2,3,4 상하좌우
'''

from collections import deque

n,m = map(int, input().split())
board = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))


dy = [-1,+1,+0,+0]
dx = [+0,+0,-1,+1]
ans = 0


'''
1(상)
1: 무시 2: 2(하) 3: 4(우) 4: 3(좌)
2(하)
1: 무시 2: 1(상) 3: 3(좌) 4: 4(우)
3(좌)
1: 4(우) 2: 무시 3: 2(하) 4: 1(상)
4(우)
1: 3(좌) 2: 무시 3: 1(상) 4: 2(하)
'''
def change_dir(d, num):
    # 방향, 물건 숫자
    if d == 0:
        if num == 1:
            return d
        elif num == 2:
            return 1
        elif num == 3:
            return 3
        elif num == 4:
            return 2
    if d == 1:
        if num == 1:
            return d
        elif num == 2:
            return 0
        elif num == 3:
            return 2
        elif num == 4:
            return 3
    if d == 2:
        if num == 1:
            return 3
        elif num == 2:
            return d
        elif num == 3:
            return 1
        elif num == 4:
            return 0
    if d == 3:
        if num == 1:
            return 2
        elif num == 2:
            return d
        elif num == 3:
            return 0
        elif num == 4:
            return 1


def bfs(y,x):
    global ans
    # 상 하 좌 우 넣기. 
    qu = deque()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=nx<m and 0<=ny<n:
            qu.append((ny,nx,i))
    while qu:
        nny, nnx, dir = qu.popleft()
        
        '''
        1. 9를 만나면 제외(어차피 나중에 또 계산함)
        2-1. visited 아니면 ans 더하기
        2-2. visited 처리하기
        3. 다음 갈 곳이 반대 방향이면 확인 x 
        4. dir 값 변경 (0이면 그대로)
        
        '''
        ### 핵심: board가 9면 더 나아갈 필요 x (visited 처리 전에)
        if board[nny][nnx] == 9:
            continue
            
        # visited 처리 및 ans 값 더하기
        if visited[nny][nnx] == 0:
            ans += 1
        visited[nny][nnx] = -1
        
        
        # 반대되는 방향 확인 x 
        if (dir == 0 or dir == 1) and board[nny][nnx] == 2:
            continue
        if (dir == 2 or dir == 3) and board[nny][nnx] == 1:
            continue
        
        # dir를 먼저 확인하자. 
        newdir = -1
        if board[nny][nnx] == 0:
            newdir = dir
        else:
            newdir = change_dir(dir, board[nny][nnx])
        
        
        nnny = nny + dy[newdir]
        nnnx = nnx + dx[newdir]
        if 0<=nnnx<m and 0<=nnny<n :
            qu.append((nnny, nnnx, newdir))

for i in range(n):
    for j in range(m):
        if board[i][j] == 9:
            visited[i][j] = -1
            ans += 1
            bfs(i,j)


print(ans)


'''
무한루프를 어떻게 깰까?
본 선풍기에 닿으면 flag를 바꾼다.
만약 본 선풍기인데 flag가 바꿔진 상태다?
그러면 무한루프 빠진거니까 빼버린다. 

다시 생각하니. 
이미 상<->하 ,좌<->우 서로 반대가 채워지기에 
굳이 넘어갈 필요는 없다. 


# 반례 확인
3 3
9 9 9
9 9 9
9 9 9

board[nny][nnx] == 9(선풍기 만났을 때의 조건)을 제일 먼저 한다.

'''