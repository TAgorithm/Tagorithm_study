from collections import deque

def count(q1, q2, s):
    q1 = deque(q1)
    q2 = deque(q2)
    for i in range(len(q1)):
        if s < q1[i]:
            return -1
    for i in range(len(q2)):
        if s < q2[i]:
            return -1
    cnt = 0
    s1 = sum(q1)
    s2 = sum(q2)
    while(cnt < 600000):
        if s == s1 == s2:
            return cnt
        elif s1 > s2:
            e = q1.popleft()
            q2.append(e)
            s1 -= e
            s2 += e
        elif s1 < s2:
            e = q2.popleft()
            q1.append(e)
            s2 -= e
            s1 += e
        cnt += 1
    return -1 
        
q1 = [1] 
q2 = [1]
print(count(q1, q2, (sum(q1) + sum(q2))//2))