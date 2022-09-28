# 욱제는 결정장애야!

n = int(input())
choice = list(map(int, input().split()))
sticker = []
count = 0
max_cnt = 0

# 돌림판 칸 수만큼 반복문 돌리기
for i in choice:
    if i not in sticker: # 스티커 안 붙어 있으면
        sticker.append(i) # 스티커 배열에 골라진 숫자 넣기
        count += 1
    else: # 붙어 있으면
        #sticker.remove(i) 시간 오래 걸림! 없어도 됨
        count -= 1
    max_cnt = max(max_cnt, count)

print(max_cnt)