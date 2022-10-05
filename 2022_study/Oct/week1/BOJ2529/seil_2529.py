# 2529 (부등호)
# 10:21~11:12
# for을 입력값에 따라 깊게 들어가기에. 재귀함수라고 생각해서 풀었다
# for문을 재귀함수에 넣고. for문 안에서 재귀함수를 다시 호출하는 식.

n = int(input())
symbol = list(input().split())
max_num = 0
min_num = 100000000000

# parms: 현재 위치, 사용한 숫자를 순서대로 담긴 arr
def recur(cur_idx, arr):
    
    global max_num
    global min_num
    # 조건에 맞는 순서식은 min,max 비교
    if cur_idx == n:
        max_num = max(max_num, int("".join(map(str, arr))))
        min_num = min(min_num, int("".join(map(str, arr))))
        return 
    for i in range(10):
        if i in arr:
            pass
        else:
            arr.append(i) # 이거 대신 visited를 쓰는 경우도 존재.
            if symbol[cur_idx] == "<" and arr[cur_idx] < i:
                recur(cur_idx + 1, arr)
            elif symbol[cur_idx] == ">" and arr[cur_idx] > i:
                recur(cur_idx + 1, arr)
            arr.pop()
                
# depth가 0인 경우도 recur에 넣는 식으로 많이 구현함. 
# if len(arr) == 0: 이런 조건으로
for i in range(10):
    recur(0, [i])

print(max_num)
# min_num의 경우 021 -> 21로 프린트 되는 문제가 있었다.
if len(str(min_num)) == n:
    print('0' + str(min_num))
else:
    print(min_num)