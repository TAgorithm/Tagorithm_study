# 프로그래머스: 타겟넘버(43165)

from collections import deque
def bfs(x, numbers, target):
    
    qu = deque()
    qu.append((x,0)) # 순서, 토탈 값
    ans = 0
    while qu:
        nx, total = qu.popleft()
        if nx == len(numbers):
            if total == target:
                ans += 1
        else:
            qu.append((nx+1, total + numbers[nx]))
            qu.append((nx+1, total - numbers[nx]))
    
    return ans
    
def solution(numbers, target):
    return bfs(0, numbers, target)


print(solution([1,1,1,1,1], 3))