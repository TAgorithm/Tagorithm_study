# 1697(숨바꼭질)
# 12:59~ 2:03 (1시간 4분)
### bfs 
# 1. bfs(0,0)으로 시작
# 2. 큐에 아무것도 없을때까지 while문으로 돌고
# 3. 큐에 계속 자식을 넣으면서 비교확인한다. 
from collections import deque


n, k = map(int, input().split())
qu = deque()
min_counts = [0] * 160000
dx = [-1, 1]
def bfs():
    while qu:
        cur = qu.popleft()
        cur_index = cur[0]
        cur_count = cur[1]
        # x-1
        if cur_index+dx[0] >= 0 and cur_index+dx[0] < 160000:
            if min_counts[cur_index+dx[0]] == 0:
                min_counts[cur_index+dx[0]] = cur_count + 1
                qu.append([cur_index+dx[0], cur_count + 1])
            else:
                if min_counts[cur_index+dx[0]] > cur_count+1:
                    min_counts[cur_index+dx[0]] = cur_count + 1
                    qu.append([cur_index+dx[0], cur_count + 1])
        # x+1
        if cur_index+dx[1] >= 0 and cur_index+dx[1] < 160000:
            if min_counts[cur_index+dx[1]] == 0:
                min_counts[cur_index+dx[1]] = cur_count + 1
                qu.append([cur_index+dx[1], cur_count + 1])
            else:
                if min_counts[cur_index+dx[1]] > cur_count+1:
                    min_counts[cur_index+dx[1]] = cur_count + 1
                    qu.append([cur_index+dx[1], cur_count + 1])
        
        # 2x
        if cur_index*2 >= 0 and cur_index*2 < 160000:
            if min_counts[cur_index*2] == 0:
                min_counts[cur_index*2] = cur_count + 1
                qu.append([cur_index*2, cur_count + 1])
            else:
                if min_counts[cur_index*2] > cur_count+1:
                    min_counts[cur_index*2] = cur_count + 1
                    qu.append([cur_index*2, cur_count + 1])
        

qu.append([n,0]) # [0]: 위치, [1]: 현 카운트
if n == k:
    ## 자기 자신일 때는 값이 0 (예외처리)
    print(0)
else:
    bfs()
    print(min_counts[k])

