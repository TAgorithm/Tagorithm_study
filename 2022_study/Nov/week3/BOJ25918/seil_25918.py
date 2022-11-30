'''
12:01 ~ 12:38 (X)
1:20-2:20 (X)

반례 찾고 해결.
O -> ()  X -> )( 
'''

N = input()
S = input()

if S.count("(") != S.count(")"):
    print(-1)
else:
    stack = []
    ans = -1
    flag = 0
    is_reverse_first = False # ")" 부터 시작
    for s in S:
        if flag < 0:
            if s == "(":
                is_reverse_first = False
                ans = max(ans, abs(flag))
                flag += 1
                continue
            else:
                flag -= 1
                ans = max(ans, abs(flag))
        else:  
            if s == "(":
                flag += 1
                stack.append("(")
                ans = max(ans, len(stack))
            elif s == ")":  
                flag -= 1
                if len(stack) != 0:
                    stack.pop()

    if flag != 0:
        print(-1)
    elif len(stack) != 0:
        # stack에 남아있으면
        print(-1)
    else:
        print(ans)
        

## 쉬운 코드
# stack을 쓸 필요가 없다.
N = int(input())
S = input().rstrip()
result = []
res = 0
for s in S:
    if s =="(":
        res+=1
    else :
        res-=1
    result.append(abs(res))

if res == 0:
    print(max(result))
else:
    print(-1)

## 반례 통과 못하는 코드 
'''
N = input()
S = input()

if S.count("(") != S.count(")"):
    print(-1)
else:
    stack = []
    ans = -1
    is_reverse_first = False # ")" 부터 시작
    for s in S:
        if is_reverse_first:
            if s == "(":
                is_reverse_first = False
                ans = max(ans, 1)
                continue
            else:
                # stack에 없는데 ")"가 2번 이상 나오면 문제 발생
                ### 여기가 문제 발생하는 곳이다. 
                ans = -1
                break
        else:  
            if s == "(":
                stack.append("(")
                ans = max(ans, len(stack))
            elif s == ")":  
                if len(stack) == 0:
                    is_reverse_first = True    
                else:
                    stack.pop()

    if is_reverse_first:
        print(-1)
    elif len(stack) != 0:
        # stack에 남아있으면
        print(-1)
    else:
        print(ans)
        
'''


# 최종 반례
'''
4
))((
2
    -> 나는 -1나온다. 
'''

# 반례 찾기
'''
(( )( ())) 3
(()(())) 3

)()()() -1 
) -1
( -1

(())) -1

2
)(
1

4
)(()
1

1
)
-1

1
(
-1
'''