n = int(input())
choice = list(map(int, input().split()))
sticker = []
count = 0
max_cnt = 0

for i in choice:
    if i not in sticker:
        sticker.append(i)
        count+=1
    else:
        count-=1
    max_cnt = max(max_cnt, count)
        
print(max_cnt)