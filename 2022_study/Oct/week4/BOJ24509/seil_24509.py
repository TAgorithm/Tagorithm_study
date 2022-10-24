# 상품의 주인은?
# 10:42-11:14
'''
혜민이네 반은 총 $N$명의 학생으로 이루어져 있으며 
학생마다 번호가 다르게 배정되어 있다. 
이번 시험은 국어, 영어, 수학, 과학 총 4과목으로, 
(1) 과목별 1등에게 상품을 주기로 했다. 
(2) 수상은 국어, 영어, 수학, 과학 순서로 하며 
(3) 학생마다 상품은 한 번만 받을 수 있다. 
예를 들어 국어 과목에서 1등 한 사람이 
수학 과목에서 또 1등을 한다면 
국어 과목에서 상품을 받았기 때문에 
이 학생은 다른 과목에서 상품을 더 받을 수 없다. 
(4) 따라서 수학 과목은 상품을 받지 않은 학생 중에 
점수가 가장 높은 학생이 상품을 받는다. 

(5) 단, 동점이 있으면 번호가 빠른 사람이 상품을 받는다. 
과목별 상 받을 사람의 번호를 출력하시오.
'''

n = int(input())

lang = [0 for i in range(n)]
eng = [0 for i in range(n)]
math = [0 for i in range(n)]
science = [0 for i in range(n)]

def getmaxstu(idx):
    max_val = -1
    max_idx = -1
    if idx == 0:
        for i in range(len(lang)):
            # 동점은 제외. 더 큰 사람만 생각
            if max_val < lang[i]:
                max_val = lang[i]
                max_idx = i
        eng[max_idx] = -1
        math[max_idx] = -1
        science[max_idx] = -1
        return max_idx+1
    elif idx == 1:
        for i in range(len(eng)):
            # 동점은 제외. 더 큰 사람만 생각
            if max_val < eng[i]:
                max_val = eng[i]
                max_idx = i
        math[max_idx] = -1
        science[max_idx] = -1
        return max_idx+1
    elif idx == 2:
        for i in range(len(math)):
            # 동점은 제외. 더 큰 사람만 생각
            if max_val < math[i]:
                max_val = math[i]
                max_idx = i
        science[max_idx] = -1
        return max_idx+1
    else:
        for i in range(len(science)):
            # 동점은 제외. 더 큰 사람만 생각
            if max_val < science[i]:
                max_val = science[i]
                max_idx = i
        return max_idx+1
        
        
        
    
for i in range(n):
    idx,l,e,m,s = map(int, input().split())
    idx += -1
    lang[idx] = l
    eng[idx] = e
    math[idx] = m
    science[idx] = s

ans = []
for i in range(4):
    ans.append(getmaxstu(i))

print(*ans)


# 반례
# 4
# 4 1 0 0 0
# 1 0 0 0 0
# 2 0 0 0 0
# 3 0 0 0 0

# 반례
# 4
# 4 22 22 22 22
# 1 22 22 22 22
# 2 22 22 22 22
# 3 22 22 22 22

