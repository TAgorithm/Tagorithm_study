from itertools import combinations

N = int(input())
material = []
subs = []

for _ in range(N):
    material.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in combinations(material, i):
        sour = 1
        bitter = 0
        for num in j:
            sour = sour * num[0]
            bitter = bitter + num[1]
        sub = abs(sour - bitter)
        subs.append(sub)

print(min(subs))