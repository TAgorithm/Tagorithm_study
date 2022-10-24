# 17952(과제는 끝나지 않아!)
# 10:26 - 10:40

'''
과제1 -> 과제2 -> 과제3 이면
과제3 다 끝내고 과제 1을 하는게 맞을까?
이전에 하던 과제라고 하니 과제2가 맞겠지?
그럼 stack으로 구현

'''
n = int(input())
homework = [] # [100, 3] 점수,남은시간(변경)
ans  = 0
while n > 0:
    n += -1
    ret = input()
    if ret == '0':
        if homework:
            cur = homework.pop()
            cur[1] += -1
            if cur[1] == 0:
                ans += cur[0]
            else:
                # 다시 넣어주기
                homework.append(cur)
        continue
    else:
        one,a,t = map(int, ret.split())
        t += -1
        if t == 0:
            ans += a
        else:
            homework.append([a,t])
        
print(ans)
    