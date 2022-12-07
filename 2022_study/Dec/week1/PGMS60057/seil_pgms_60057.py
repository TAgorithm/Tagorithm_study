# 프로그래머스: 문자열 압축(60057)
# 4:49- 시간 오래 걸림.

'''
1,2,3, ... 이 순으로? 

2개로 짜르면 무조건 2개만 가능.
3개 단위로  짜르면 3개로만 가능한 것. 

s/2 까지 진행. 
'''

# 해결 과정
'''
생각보다 어려웠다. 특히 케이스 5번처럼.
맨 처음부터 나눠져야한다는 점이 이해하기 어려웠다.

token화하는 것을 처음 배웠다. 
wrap 사용할 것. (혹은 slice 활용.) 
'''

s = 'aabbaccc'
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"
s = "aaaaaaaaaabbbbbbbbbb"
s = '1'

## 2번째 풀이

from textwrap import wrap
import re

ans = 1001
for i in range(1,len(s)//2+1):
    tokens = wrap(s, i)
    cur = tokens[0]
    restr = ""
    recnt = 1
    j = 0
    while j < len(tokens)-1:
        j += 1
        if cur == tokens[j]:
            recnt += 1
        else:
            if recnt > 1:
                restr += str(recnt) + cur
            else:
                restr += cur
            cur = tokens[j]
            recnt = 1
    
    # 마지막 남은 것 넣어줄 것.
    if recnt > 1:
        restr += str(recnt) + cur
    else:
        restr += cur
    ans = min(ans, len(restr))

if ans == 1001:
    # return len(s)
    print(len(s))   
else:
    print(ans)   
        


## 1번째 풀이
# 맨 앞부터 분리 안해도 되도록 하는 방법
'''
s = 'aabbaccc'
s = "ababcdcdababcdcd"
s = "abcabcdede"
s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd" # 이게 안 풀리는데? 

from collections import deque

ans = 1001
for i in range(1,len(s)//2):
    # i가 길이 기준.
    result = len(s)
    qu = deque() # 기준 qu.
    j = -1
    while j < len(s)-1:
        j += 1
        # 원소 s[j]
        if len(qu) < i:
            qu.append(s[j])
        else:
            # 맨 앞 빼고. 뒤에 넣고.
            # i+1, i+2 ... 등이랑 비교해서 같은지 확인? 
            repeat = True
            for k in range(1,i+1):
                # indexoutofbound
                if j+k >= len(s):
                    repeat = False
                    break
                if qu[k-1] == s[j+k]:
                    continue
                else:
                    repeat = False
                    break
                    
            
            if repeat:
                j += i # 다음 j는 넘기기.
                result -= i
            else:
                qu.popleft()
                qu.append(s[j])
                # 맨 앞 pop, 맨 뒤에 add? 
                    
    ans = min(ans, result)


print(ans)

'''