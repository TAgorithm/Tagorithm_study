import sys

N = int(sys.stdin.readline())

std = []

for _ in range(N):
    score = list(map(int, sys.stdin.readline().split()))
    std.append(score)

idx = [-1, -1, -1, -1]

std.sort()

for i in range(1, 5):
    max = -1
    for j in range(N):
        if std[j][0] not in idx:
            if max < std[j][i]:
                max = std[j][i]
                idx[i-1] = j+1
print(*idx)