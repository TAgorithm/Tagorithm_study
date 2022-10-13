import sys
from collections import defaultdict

case = int(input())

def sumlength(lengthlist, i):
    if i == 0:
        return lengthlist[0]
    return lengthlist[i] * sumlength(lengthlist, i-1)

for i in range(case):
    n = int(input())
    if n == 0:
        print(0)
        continue
    clothes = defaultdict(list)
    for j in range(n):
        name, type = map(str, sys.stdin.readline().split())
        clothes[type] += [name]
    lengths = [len(v)+1 for v in clothes.values()]
    print(sumlength(lengths, len(lengths)-1) - 1)