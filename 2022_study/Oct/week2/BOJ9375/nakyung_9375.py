import sys
input = sys.stdin.readline

T = int(input())
result = 1

for _ in range(T):
    num = int(input())
    dict = {}

    for _ in range(num):
        n, m = map(str, input().split()) # n = 의상 이름, m = 의상 종류

        if m in dict.keys():
            dict[m].append(n)
        else:
            dict[m] = [n, ""] # ""는 안 입은 경우
    
    for key in dict.keys():
        result *= len(dict[key])

    print(result - 1)
    result = 1 # 다시 숫자 초기화해 주기