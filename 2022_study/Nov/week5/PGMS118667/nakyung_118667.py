# pop(0)은 시간초과 발생, popleft() 써주어야 한다
# deque 사용

from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1, q2 = 0, 0
    
    # 각 큐의 합
    for i in queue1:
        q1 += i
    for i in queue2:
        q2 += i
        
    hab = (q1 + q2) / 2

    queue1, queue2 = deque(queue1), deque(queue2)
    
    # 빼고 넣을 숫자
    num = 0
    
    for _ in range(3 * len(queue1)):            
        if q1 > hab:
            num = queue1.popleft()
            queue2.append(num)
            q1 -= num
            q2 += num
            answer += 1
        elif q1 < hab:
            num = queue2.popleft()
            queue1.append(num)
            q1 += num
            q2 -= num
            answer += 1
        else:
            return answer
    
    return -1