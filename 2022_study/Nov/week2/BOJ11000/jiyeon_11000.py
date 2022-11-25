'''
끝나는 시간을 값으로 해서 다시 구현해보기 
'''
import sys
import heapq

N = int(sys.stdin.readline())

time = []
for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key = lambda x : (x[0], x[1]))
queue = []

for start, end in time:
    if len(queue) == 0:
        heapq.heappush(queue, end)
        continue
    qend = heapq.heappop(queue)
    if qend <= start:
        heapq.heappush(queue, end)
    else:
        heapq.heappush(queue, qend)
        heapq.heappush(queue, end)

print(len(queue))
