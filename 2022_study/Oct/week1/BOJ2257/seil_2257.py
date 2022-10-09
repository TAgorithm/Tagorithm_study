# 2257 (화학식량)

word = input()
dict = {"H": 1, "C":12, "O":16}
visited = [0] * len(word)
def cal(start):
    val = 0
    for i in range(start, len(word)):
        if visited[i] == -1:
            continue
        if word[i] == "(":
            visited[i] = -1
            val += cal(i+1)
        elif word[i] == ")":
            # 곱한 계산 리턴
            if i+1 < len(word) and word[i+1].isdigit():
                # ")" 뒤에 숫자가 없을수도
                visited[i] = -1
                visited[i+1] = -1
                return  val *int(word[i+1])
            else:
                visited[i] = -1
                return val
        else:
            if i+1 < len(word) and word[i+1].isdigit() and word[i+1] != ")":
                # i, i+1 visited 변경
                val += dict[word[i]] * int(word[i+1])
                visited[i], visited[i+1] = -1, -1
            else:
                val += dict[word[i]]
                visited[i] = -1
                
    return val

print(cal(0))

### 리뷰 
# visited를 통해 방문한 곳은 패스할 수 있는 방법이 있었다. 


### 코드 짜면서 한 생각
# 깊이탐색 같기도하고. 
# 근데 깊이탐색은 다 돌면서 이미 visited면 안하는 식이지 않나?
# 깊이탐색이지만 너비탐색처럼 식을 구성? => cal(0)하고 끝나는 부분처럼.


### 처음 생각한 코드
# 깊이, 남은string
# def cal(s):
#     val = 0 # 값
#     pass_cnt = 0 # 패스할 갯수
#     cur_pass_cnt = 0 # 현재 함수에서 패스할 함수
#     for i in len(s):
#         if pass_cnt > 0:
#             pass_cnt += -1
#             continue
#         if s[i] == "(":
#             cal(dep +1, 0) # 숫자로 나온다. 
#             # 가장 멀리 있는 )
#         elif s[i] == "H":
#             val += 1
#         elif s[i] == "C":
#             val += 12
#         elif s[i] == "O":
#             val += 16
#         elif s[i] == ")":
#             # 값 계산해서 return 
#             return val, pass_cnt
#         pass_cnt +=1

# cal(word)



## 준서 코드
# 스택을 활용한 코드
import sys

molecule = list(map(str,sys.stdin.readline().strip()))
molecular_weight = [ ]

for i in molecule:
    if i == '(' :
        molecular_weight.append(i)
    elif i == ')':
        s = 0
        while True :
            v = molecular_weight.pop()
            if v == '(':
                break
            s += v
        molecular_weight.append(s)
    
    elif i == 'H':
        molecular_weight.append(1)
    elif i == 'C':
        molecular_weight.append(12)
    elif i == 'O':
        molecular_weight.append(16)
    
    else : #숫자
        molecular_weight[-1] *= int(i)

print(sum(molecular_weight))
