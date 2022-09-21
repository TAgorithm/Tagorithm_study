# 9:52 ~ 10:20
# 1966 (프린터 큐)
from collections import deque
n = int(input())

for i in range(n):
    length,index = map(int, input().split())
    qu = deque() # [1,2,3,4]
    count = 0
    ### list 값 qu에 넣는 방법.? 
    for v in list(map(int, input().split())):
        qu.append(v)
    
    while True:
        cur = qu.popleft()
        ### 하나 남은 걸 뽑은 경우
        # if len(qu) == 0:
        if not qu:
            count += 1
            break
        ### 중요도가 가장 높은 값일 경우 제외, index -1 이동
        ### 단, index가 -1이면 원했던 값이기에 break(탈출)
        if cur >= max(qu):
            count += 1
            index -= 1
            if index == -1:
                break
        else:
            ### 1. qu 다시 뒤에 넣기 2. index 이동
            qu.append(cur)
            if index == 0:
                index = len(qu) - 1
            else:
                index -= 1
    print(count)
    

### 풀이 2
## 기준: 뽑는 숫자의 index가 0일 때, 아닐 때로 구분.
def solve():
    n, m = map(int, sys.stdin.readline().split())
    docs = list(map(int, sys.stdin.readline().split()))
    queue = deque(docs)
    cnt = 0
    while queue:
        x = queue.popleft()
        if m == 0:
            if not queue or x >= max(queue):
                print(cnt + 1)
                return
            else:
                m += len(queue)
                queue.append(x)
        else:
            m += -1
            if not queue or x >= max(queue):
                cnt += 1
            else:
                queue.append(x)