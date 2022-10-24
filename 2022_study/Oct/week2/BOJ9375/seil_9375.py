# 패션왕 신해빈 (9375)
# 5:48 - 6:00
import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    dict = {}
    for _ in range(int(input())):
        name, cate = input().split()
        if cate not in dict:
            dict[cate] = [name]
        else:
            dict[cate].append(name)
    
    ans = 1
    for key in dict:
        ans *= (len(dict[key])+1)
    
    # 3*2-1 = 5 (경우의수 문제)
    print(ans - 1)
    
    

import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    tmp_lst =[]
    res = 1
    for _ in range(n):
        _, cls = input().split()
        tmp_lst.append(cls)
    tmp_lst_var = set(tmp_lst)
    if len(tmp_lst_var) == 1 :
        res = n 
        print(res)
    else:
        for var in tmp_lst_var:
            a = tmp_lst.count(var)
            res *= a+1
        print(res-1)