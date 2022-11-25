import sys

N, S, R = map(int,sys.stdin.readline().split())

damage = list(map(int,sys.stdin.readline().split()))

extra = list(map(int,sys.stdin.readline().split()))

damage.sort()
extra.sort()

for num in extra:
    if num in damage:
        damage.remove(num)
    elif num-1 in damage:
        damage.remove(num-1)
    elif num+1 in damage: 
        damage.remove(num+1)
        
print(len(damage))