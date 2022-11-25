import sys

N = int(sys.stdin.readline())

bear = list(sys.stdin.readline().strip())

if N % 2 == 1:
    print(-1)
else:
    result = [0]*(N+1)
    res = 0
    for i in range(N):
        if bear[i] =="(":
            result[i+1] = result[i] + 1
        else :
            result[i+1] = result[i] - 1
    
    for i in range(N):
        result[i+1] = abs(result[i+1])

    if result[N] == 0:
        print(max(result))
    else:
        print(-1)