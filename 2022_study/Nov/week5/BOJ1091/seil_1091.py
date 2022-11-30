# 카드섞기 1091 

'''
6:48~ 7:13 (X)
1:10-1:24 (O)

핵심:
player는 3명. 각 플레이어는 여러개의 카드를 가진다.
ex. 카드 12개면 초기에
p1: [0,3,6,9] / p2: [1,4,7,10] / p3: [2,5,8,11]
'''

n = int(input())
P = list(map(int, input().split())) # 정답
S = list(map(int, input().split()))

ans = [[] for _ in range(3)]
for i in range(n):
    ans[P[i]].append(i)

change = [k for k in range(n)]
cnt = 0
exit = False
first = True
while not exit:
    
    # 첫번째 로직 제외
    # 탈출 구문1: 다시 원래 식으로 돌아오면 해당사항 없음 
    if first:
        first = False
    else:
        
        if change == [k for k in range(n)]:
            cnt = -1
            break
    exit = True
    
    
    # 탈출 구문2: 하나라도 안 맞으면 exit=False
    for l in range(n):
        if change[l] not in ans[l % 3]:
            exit = False
            break
            
    if exit:
        break
    
    
    # 횟수 + 1         
    cnt += 1
    
    
    # 값 변경 
    new_change = [0] * n
    for j in range(n):
        new_change[S[j]] = change[j]
    change = new_change
    

print(cnt)
    

