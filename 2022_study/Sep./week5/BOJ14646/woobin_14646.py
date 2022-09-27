import sys
input = sys.stdin.readline

n = int(input()) # 3
arr = list(map(int, input().split())) # [1 3 3 2 1 2]
visited = [False] * n 
cnt = 0

answer = 0
for i in arr:
    if not visited[i-1]:
        cnt += 1
        visited[i-1] = True
    else:
        cnt -= 1
        visited[i-1] = False
    answer = max(answer, cnt)
    
    if answer == n:
        break

print(answer)