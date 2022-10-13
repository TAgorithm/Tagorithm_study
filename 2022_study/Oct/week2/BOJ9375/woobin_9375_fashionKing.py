import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        _, key = input().split()
        if key in clothes:
            clothes[key] += 1
        else:
            clothes[key] = 1

    anw = 1
    if len(clothes) == 1:
        anw = clothes[key]
        print(anw)
    else:
        for i in clothes:
            anw *= (clothes[i]+1)
        print(anw-1)
