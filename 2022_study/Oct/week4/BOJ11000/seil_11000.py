# 10:08~11:00 (못 품)
'''
10^9라서 모든 항목 for문 도는건 시초날 듯.
20만 * 10억. 

1 3 
2 10
3 4
3 5
1 3 (100개) 

먼저 sort를 한다면? 

'''
'''
11:44-12:06 (두번째 생각.)
1 4
2 3 새로운 start 2가 4보다 작으니 4를 가지고 cnt는2
=> i=2이다. 만약 end가 i+1이면 Pop (선형탐색) O(n)
pop하면 cnt += -1 

3 4 새로운 start 3이 4보다 작으니 4를 가지고 cnt는3
4 6 새로운 start 4가 4보다 크거나 작으니 다시 cnt는 3?


1 10 stack에 넣어.
2 5 stack에 넣어.
5 9 stack과 비교하면서 현재 start보다 end가 작은 값들 빼버리기.
stack에 넣어. 
8 12
12 20

6
1 10
2 6
3 6
4 7
12 20
13 15
'''

# n = int(input())
# stack = []
# ans = 0
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
# arr.sort()
# for a in arr:
#     if not stack:
#         stack.append(a)
#     else:
#         new_stack = []
#         cs, ce = a[0], a[1]
#         for s in stack:
#             if cs < s[1]:
#                 new_stack.append(s)
#         new_stack.append([cs, ce])
#         stack = new_stack
#         ans = max(ans, len(new_stack))

# print(ans)


# 문제 해설.
'''
13
1 10
2 6
3 6
4 7
12 20
13 15
20 25
25 50
26 47
27 44
28 41
29 39 # 여기부터 다시 추가. (최소값이 41이니까)
30 35 # 여기도 추가.

'''
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

