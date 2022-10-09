# 10819 (차이를 최대로)
# 2:30~3:14
# 완탐 ( n < 8 )
# 순열의 모든 경우를? 
ans = 0
n = int(input())
arr = list(map(int, input().split()))

def cal(x,y):
    return abs(x-y)

def recur(visited, cur_arr):
    global ans
    if len(cur_arr) == n:
        cur_sum = 0 
        for i in range(len(cur_arr)-1):
            cur_sum += cal(cur_arr[i], cur_arr[i+1])
        ans = max(ans, cur_sum)
    
    # 배열 추가
    for i in range(n):
        if visited[i] == -1:
            pass
        else:
            visited[i] = -1
            cur_arr.append(arr[i])
            recur(visited, cur_arr)
            visited[i] = 0
            cur_arr.pop()
        

# visited, 현재배열 
recur([0]*n, [])
print(ans)

## 처음 코드 
# from functools import reduce
# ans = 0
# n = int(input())
# arr = list(map(int, input().split()))

# def cal(x,y):
#     return abs(x-y)

# def recur(cur_arr):
#     global ans
#     if len(cur_arr) == n:
#         cur_sum = 0 
#         for i in range(len(cur_arr)-1):
#             cur_sum += cal(cur_arr[i], cur_arr[i+1])
#         ans = max(ans, cur_sum)
    
#     # 배열 추가
#     for v in arr:
#         if v in cur_arr:
#             pass
#         else:
#             cur_arr.append(v)
#             recur(cur_arr)
#             cur_arr.pop()
        

# # 현재 더한값, 이미 쓴 배열
# recur([])
# print(ans)

# 모든 경우의 배열을 만들고. 값을 비교?

# 문제 -> 같은 값인 경우 
# 반레 0 2 2 -> 4




# arr = [1,2,3]
# print(list(map(lambda x, y: abs(x-y), arr)))

# numbers = [0,1,2,3]
# print(list(map(lambda x: x > 0, numbers)))