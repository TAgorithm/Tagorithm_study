num = int(input())

for i in range(num):
    N, M = map(int, input().split())
    que = list(map(int, input().strip().split()))
    que = [(value, idx) for idx, value in enumerate(que)]
    cnt = 0

    while True:
        m = max(que)[0]
        if que[0][0] == m:
            cnt += 1
            if que[0][1] == M:
                print(cnt)
                break
            que.pop(0)
        else:
            que.append(que.pop(0))