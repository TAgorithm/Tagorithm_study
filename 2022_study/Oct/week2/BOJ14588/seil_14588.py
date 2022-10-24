# Line Friends Small (14588)
# 12:03~ 1:43 (못 풀었다.) => bfs로 변경해보자.
# 결국 해결.

# dfs -> bfs로 변경 후, 27%까지 상승
# 결국 가장 endpoint가 큰 값만 qu에 넣어주는 것이 정답이었다.
# 맨 처음 생각은 겹치는 모든 친구를 다 넣어줬다. 
# 그 이유는
# 1.      --------
# 2.   -----
# 3. ----
# 4. ------------------- ... 
# 1번에서 4번으로 가서 쭉 길게 가는 경우도 있겠다고 생각함.
# 하지만 4번 역시 1번의 친구가 될 수 밖에 없음을 알게 되었고.
# 무조건 조건에 맞는 것 중에 가장 우측으로 긴 친구만 넣어도 되는 것을 알게 되었다.

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lines = []
min_val = 1000000000002
for _ in range(n):
    lines.append(list(map(int, input().split())))

def bfs(f_sf1, f_cnt, ef2):
    global min_val
    qu = deque()
    qu.append([f_sf1, f_cnt])
    # 탈출
    while qu:
        cur = qu.popleft()
        sf1 = cur[0]
        cnt = cur[1]
        if ef2[0] <= sf1[1]:
            min_val = min(min_val, cnt)
        else:
            # 친구를 다 넣어서 bfs를 다시 돌린다.
            # 단 방문한 친구와 자기 자신은 다시 넣지 않도록 한다.
            # 자신보다 큰 친구만 넣는다.
            max_range_idx = 0
            max_range = -1000000000
            for i in range(n):
                # 조건: 겹치고, 조금이라도 길 경우. 
                # ------
                #       -------   (1)
                # -------         (2)
                if lines[i][0] <= sf1[1] and lines[i][1] > sf1[1]:
                    # 가장 긴 값의 index를 탐색
                    if lines[i][1] > max_range:
                        max_range_idx = i
                        max_range = lines[i][1]
            
            if max_range != -1000000000:       
                # 만약 max_range가 값이 그대로면 조건에 맞는 것이 하나도 없는 것. (flag)
                qu.append([lines[max_range_idx], cnt+1])
            
# 문제를 n번 푼다.
for _ in range(int(input())):
    min_val = 1000000000002
    f1, f2 = map(int, input().split())
    # end점이 더 큰 값을 찾아가는 target으로 둔다.
    if lines[f1-1][1] < lines[f2-1][1]:
        bfs(lines[f1-1], 1, lines[f2-1])
    else:
        bfs(lines[f2-1], 1, lines[f1-1])
    
    # 못 찾아갔으면 -1
    if min_val == 1000000000002:
        print(-1)
    else:
        print(min_val)
        

### 모든 친구를 방문하는 dfs 코드

# import sys
# input = sys.stdin.readline
# n = int(input())
# lines = []
# min_val = 1000000000002
# for _ in range(n):
#     lines.append(list(map(int, input().split())))

# def dfs(sf1, ef2, cnt, first):
#     global min_val
#     # 탈출
#     if ef2[0] <= sf1[1]:
#         min_val = min(min_val, cnt)
#     else:
#     # 친구를 다 넣어서 dfs를 다시 돌린다.
#     # 단 방문한 친구와 자기 자신은 다시 넣지 않도록 한다.
#     # 자신보다 큰 친구만 넣는다.
#         for i in range(n):
#             # 자기 자신
#             if sf1 == lines[i]:
#                 continue
#             # 첫 방문 # 방문한 경우는 visited의 값과 비교해 min이면 추가해준다.
#             elif lines[i][1] >= sf1[1] and lines[i][0] <= sf1[1] and lines[i][1] > first[1]:
#                 if visited[i] == 0 or visited[i] > cnt:
#                     visited[i] = cnt+1
#                     dfs(lines[i], ef2, cnt+1, first)
            
# # 문제를 n번 푼다.
# for _ in range(int(input())):
#     min_val = 1000000000002
#     visited = [0] * n # 방문기록+몇번째로 온 것인지에 대한 min값
#     f1, f2 = map(int, input().split())
#     # end점이 더 큰 값을 찾아가는 target으로 둔다.
#     if lines[f1-1][1] < lines[f2-1][1]:
#         dfs(lines[f1-1], lines[f2-1], 1, lines[f1-1])
#     else:
#         dfs(lines[f2-1], lines[f1-1], 1, lines[f1-1])
    
#     # 못 찾아갔으면 -1
#     if min_val == 1000000000002:
#         print(-1)
#     else:
#         print(min_val)


### 생각3. visited의 문제
# 3 -> 2 -> 4 에서 4를 visited처리하면
# 2 -> 4 에서 막히기 때문.
# dfs -> bfs로 해야하나. 
# 아니면 count를 비교하는 로직을 구현해야하나?

### 생각2. 가지치기
# 만약 n 위치에서 가장 긴 값이 target이랑 겹치면 
# break하고 cnt를 min과 비교
# 하지만 그게 아니라면 살아있는 간선으로 둔다. 

### 생각1. 
# 앞으로 가야하면 겹치면서 가장 긴 값을
# 뒤로 가야하면 겹치면서 뒤로 가장 긴 값을
# 무조건 앞으로 가도록 target의 위치를 f2로 만들었다.