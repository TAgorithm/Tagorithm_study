import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1]) # 끝나는 시간 삽입

for i in range(1, n):
    if q[i][0] < room[0]: # 다음 회의 시작시간 < 제일 왼쪽의 저장된 회의실 끝나는 시간(room[0]) (다음 회의 시작시간이 빠르면, 작으면)
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
        # 이때 시간이 짧은 노드(최소값)가 루트노드로 이동함.
        
    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, q[i][1])

print(len(room))