# 14646 (욱제는 결정장애야!!)
# 8:09 - 8:49
# 문제 이해하기 진짜 힘들었음. 

# 모든 시점에서 가장 스티커가 많이 붙어있는 개수

### 해결
# 문제의 조건 잘 적용할 것. (<100000)
# 한번 한 것을 구분짓기 위한 마스킹용 배열을 만든다
# 그러면 스티커를 넣었다, 뺐다할 로직 필요 x
n = int(input())

count = 0
cur = 0
order = list(map(int, input().split()))
menu = [0] * 100001
for v in order:
    if menu[v] == 0:
        menu[v] = 1
        cur += 1
        count = max(count, cur)
    else:
        cur += -1

print(count)

a= [1,2,3]


## 시간초과 1
# n = int(input())
# count = 0
# cur = 0
# menu = list(map(int, input().split()))
# sticker = []
# for v in menu:
#     if v not in sticker:
#         sticker.append(v)
#         cur += 1
#         count = max(count, cur)
#     else:
#         del sticker[sticker.index(v)]
#         cur += -1

# print(count)

## 시간초과 2 (새로 짠 코드지만, 더 오래걸림.)
# n = int(input())
# count = 0
# cur = 0
# menu = list(map(int, input().split()))
# sticker = []
# for v in menu:
#     has = False
#     for j in range(len(sticker)):
#         if v == sticker[j]:
#             has = True
#             del sticker[j]
#             cur += -1
#             break
#     if has == False:
#         sticker.append(v)
#         cur += 1
#         count = max(count, cur)
        
# print(count)

## 시간초과 3 
# n = int(input())
# count = 0
# cur = 0
# menu = list(map(int, input().split()))
# sticker = []
# for v in menu:
#     try:
#         del sticker[sticker.index(v)]
#         cur += -1
#     except ValueError:
#         sticker.append(v)
#         cur += 1
#         count = max(count, cur)

# print(count)


# 순서대로 넣고, 사전순으로 확인하도록? 
# 이진탐색?


