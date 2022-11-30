'''
2021 카카오 채용연계형 인턴십: 거리두기 확인하기
4:36-5:48 (X)
최소횟수 / 두 큐 원소 합 같도록

bfs 라고 판단함. 
q1에서 빼고 q2에 넣고
q2에서 빼고 q1에 넣고 2가지 경우 존재.

탈출구문:
1. 한쪽이 빈 큐일 때; 해당 가지는 삭제 -> 무조건 1가지 경우만 넣는다.
2. mid 값과 q1,q1가 같을 때. min으로 교체
3. 최소 count보다 높아지면 탈출
4. 어떤 것들이 무한루프에 빠질 수 있지만,
5. 3번 조건에 의해서 괜찮아지지 않을까.. 
6. length가 같고 4,4로. q1 = nq2, q2 = nq1이면?
7. 그리고 appendleft를 써볼까..? 합이 차이가 안나는걸 먼저 계산?
'''

## 윤현 풀이 (좋은 방법)
'''
qu 합이 큰 쪽에서 작은 쪽으로 계속 원소를 이동시켜서 맞춘다. 
무조건 큰 쪽에서 작은 쪽
'''

from collections import deque 

def solution(queue1, queue2):
    answer = 0 
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    q1q2 = q1_sum + q2_sum 
    if q1q2 % 2 !=0:
        # 홀수면 같을 수 없다
        answer = -1 
    else:
        cnt = 0
        # qu의 최대 길이가 30만. 
        # 따라서 cnt가 60만이 최대라고 생각해서 풀었다.
        # 하지만 이 부분이 애매하다. 
        while cnt < 600000:
            cnt += 1
            if q1_sum > q2_sum:
                val1 = q1.popleft()
                q2.append(val1)

                q1_sum -=val1
                q2_sum +=val1

                answer+=1 
            elif q1_sum < q2_sum:
                val2 = q2.popleft()
                q1.append(val2)

                q1_sum += val2 
                q2_sum -= val2 

                answer+=1 
            else:
                return answer
        return -1


## 기존 풀이(시간초과 나는 풀이)
'''
# 우선 qu를 복사해서 다시 qu에 넣는 행위가 효율적이지 못함

from collections import deque
import copy

# queue1 = [3,2,7,2]
# queue2 = [4,6,5,1]

queue1 = [1,1]
queue2 = [1,5]

queue1 = deque(queue1)
queue2 = deque(queue2)


def bfs(q1, q2):
    mid = (sum(q1) + sum(q2)) // 2
    qu = deque()
    ans = 1000000000000
    cnt = 0
    fq1 = copy.copy(q1)
    fq2 = copy.copy(q2)
    qu.append((fq1, fq2, cnt))
    first = True
    while qu:
        nq1, nq2, ncnt = qu.popleft()
        
        if sum(nq1) == sum(nq2) == mid:
            ans = min(ans, ncnt)
        elif not first and ((nq1 == q2 and nq2 == q1) or (nq1 == q1 and nq2 == q2)):
            # 서로 자리가 뒤바뀐 것. 
            continue
        else:
            first = False
            # 현재 cnt가 ans보다 작은 것만 계산
            if ans > ncnt:
                if len(nq1) != 0 and len(nq2) != 0:
                    # 1
                    q1v = nq1.popleft()
                    nq2.append(q1v)
                    nnq1 = copy.copy(nq1)
                    nnq2 = copy.copy(nq2)
                    qu.append((nnq1, nnq2, ncnt+1))
                    q2v = nq2.pop()
                    nq1.append(q2v)
                    # 2
                    q2v = nq2.popleft()
                    nq1.append(q2v)
                    nnq3 = copy.copy(nq1)
                    nnq4 = copy.copy(nq2)
                    qu.append((nnq3, nnq4, ncnt+1))
    return ans    
                
        
        

answer = bfs(queue1, queue2)
if answer == 1000000000000:
    print(-1)
else:
    print(answer)
'''

