# 욱제는 결정장애야! (14646) --> 성공
# import sys

# n = int(input())
# menu = list(map(int, sys.stdin.readline().split()))
# dolimpan = [False] * (n+1)

# sticker = []

# for i in menu:
#     if sticker == n:
#         break 
#     else:
#         if dolimpan[i] == False:
#             dolimpan[i] = True
#         else:
#             dolimpan[i] = 0

#     sticker.append(sum(dolimpan))

# print(max(sticker))

#---------------------------
import sys

n = int(input())
menu = list(map(int, sys.stdin.readline().split()))
dolimpan, sticker = [], []

stick = 0

for i in menu:
    if stick == n:
        break
    else:
        if i in dolimpan:
            stick -= 1
        else:
            dolimpan.append(i)
            stick += 1
        sticker.append(stick)

print(max(sticker))


        

