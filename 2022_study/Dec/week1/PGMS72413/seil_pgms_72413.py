# 프로그래머스: 합승택시요금(72413)
# 12:48
# -2:22 정답같지만, 시간초과가 난다. 
# 플루이드 바텀업 접근

## 4번 풀이
# 플루이드 바텀업 접근

n = 6
s= 4
a=6
b=2
fares=[[4,1,10],[3,5,24],[5,6,2],[3,1,41],[5,1,20],[4,6,50],[2,4,66],[2,3,22],[1,6,25]]

board = [[1000000000 for _ in range(n+1)] for _ in range(n+1)]

# 기본 접근 값
for i in range(n+1):
    board[i][i] = 0

for f in fares:
    board[f[0]][f[1]] = f[2]
    board[f[1]][f[0]] = f[2]

# u->v 갈때 중간 k를 거치며 가는 최단거리 값
for k in range(1,n+1):
    for u in range(1, n+1):
        for v in range(1, n+1):
            board[u][v] = min(board[u][v], board[u][k] + board[k][v])


answer = 1000000000
for k in range(1,n+1):
    answer = min(answer, board[s][k] + board[k][a] + board[k][b])

print(answer)

## 생각의 흐름 정리
'''
fares = c d f
c,d -> f
4,1 = 1,4
순서 상관 없음. 
sort해야할 수도.
'''

'''
4->2,1,6 다 갈 수 있다.
2는 B지점. 그 다음 A만 찾아간다.

최소 중간 지점을 찾는 느낌인데. 

S에서 갈 수 있는 포인트는 4,1,3,5,6,2이다. 
B가 갈 수 있는 포인트는 3,1,5,6,4
A가 갈 수 있는 포인트는 자기자신 포함 6개.

각각의 최소값 구하고. 3개 값을 더하면 값이 나오지 않을까. 
지점 갯수가 200개니까. 못 가는 점은 -1. 아니면 값을 넣도록.? 
bfs 돌리도록한다. 
vitisted가 필요할까..? 최소값 구하는거니까 패스?
'''

## 3번 풀이
# 맞는듯 하나, 시간초과가 난다. (2시간)
'''
from collections import deque

def bfs(b):
    qu = deque()
    qu.append((b,0))
    arr = [10000000000] * (n+1)
    visited = [0] * len(fares) # 첫번째 visited로 했다가 변경
    
    # 자기자신 점 0으로 초기화
    arr[b] = 0
    
    while qu:
        c,v = qu.popleft() # cur지점, 지나온 past지점, value합
        for i in range(len(fares)):
            if fares[i][0] == c:
                if visited[i] == 0 or (arr[fares[i][1]] > fares[i][2]+v):
                    arr[fares[i][1]] = min(arr[fares[i][1]], fares[i][2]+v)
                    visited[i] = -1
                    qu.append((fares[i][1],fares[i][2]+v))
            elif fares[i][1] == c:
                if visited[i] == 0 or (arr[fares[i][0]] > fares[i][2]+v):
                    arr[fares[i][0]] = min(arr[fares[i][0]], fares[i][2]+v)
                    visited[i] = -1
                    qu.append((fares[i][0],fares[i][2]+v))
    return arr
        



aarr = bfs(a) 
barr = bfs(b) 
sarr = bfs(s) 

ans = 30000000000
for i in range(n+1):
    ans = min(ans, aarr[i] + barr[i] + sarr[i])

print(ans)
'''


## 2번 풀이
'''
from collections import deque

def bfs(b):
    qu = deque()
    qu.append((b,0,0))
    arr = [10000000000] * (n+1)
    
    # 자기자신 점 0으로 초기화
    arr[b] = 0
    
    while qu:
        c,p,v = qu.popleft() # cur지점, 지나온 past지점, value합
        for i in range(len(fares)):
            if fares[i][0] == c and p != fares[i][1]:
                arr[fares[i][1]] = min(arr[fares[i][1]], fares[i][2]+v)
                qu.append((fares[i][1],fares[i][0],fares[i][2]+v))
            elif fares[i][1] == c and p != fares[i][0]:
                arr[fares[i][0]] = min(arr[fares[i][0]], fares[i][2]+v)
                qu.append((fares[i][0],fares[i][1],fares[i][2]+v))
    return arr
        



aarr = bfs(a) 
barr = bfs(b) 
sarr = bfs(s) 

ans = 30000000000
for i in range(n+1):
    ans = min(ans, aarr[i] + barr[i] + sarr[i])

print(ans)
'''



## 1번 풀이
'''
from collections import deque

def bfs(b):
    qu = deque()
    qu.append((b,0))
    arr = [10000000000] * (n+1)
    visited = [0] * len(fares) # 첫번째 visited로 했다가 변경
    
    # 자기자신 점 0으로 초기화
    arr[b] = 0
    
    while qu:
        c,v = qu.popleft() # cur지점, 지나온 past지점, value합
        for i in range(len(fares)):
            if fares[i][0] == c and visited[i] == 0:
                arr[fares[i][1]] = min(arr[fares[i][1]], fares[i][2]+v)
                visited[i] = -1
                qu.append((fares[i][1],fares[i][2]+v))
            elif fares[i][1] == c and visited[i] == 0:
                arr[fares[i][0]] = min(arr[fares[i][0]], fares[i][2]+v)
                visited[i] = -1
                qu.append((fares[i][0],fares[i][2]+v))
    return arr
        



aarr = bfs(a) 
barr = bfs(b) 
sarr = bfs(s) 

ans = 30000000000
for i in range(n+1):
    ans = min(ans, aarr[i] + barr[i] + sarr[i])

print(ans)
'''



## 예제 케이스
# n=7
# s=3
# a=4
# b=1
# fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

# n=6
# s=4
# a=5
# b=6
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

# n=4
# s=1
# a=2
# b=3
# fares = [[1,2,1],[1,3,1],[1,4,100],[2,3,1],[2,4,1],[3,4,1]]