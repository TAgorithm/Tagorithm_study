### 과제는 끝나지 않아!!!

import sys
input = sys.stdin.readline

M = int(input()) # 이번 학기 몇 분인지

# 과제 점수 들어 있는 스택
score = []
# 남은 시간 들어 있는 스택
minute = []

result = 0

# M만큼 반복
for i in range(M):
    # A: 과제 만점, T: 과제 해결 걸리는 시간
    str = input()
    one = int(str.split()[0])

    if (one == 0):
        if (len(minute) != 0):
            M = M - 1 # 총 나의 시간 빼기
            minute[-1] = minute[-1] - 1 # 맨 마지막에 들어온 것 1분 빼기
            if (minute[-1] == 0):
                result += score.pop()
                minute.pop()
    else:
        A = int(str.split()[1])
        T = int(str.split()[2]) 
        score.append(A) # 과제 주어졌을 때 추가
        minute.append(T) # 걸리는 시간 추가
        if (len(minute) != 0):
            M = M - 1 # 총 나의 시간 빼기
            minute[-1] = minute[-1] - 1 # 맨 마지막에 들어온 것 1분 빼기
            if (minute[-1] == 0):
                result += score.pop()
                minute.pop()
print(result)