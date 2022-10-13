import sys

T = int(input()) #개수 입력

def factorial(n, s): #팩토리얼 구해주는 함수
    if n == s:
        return s
    return n * factorial(n-1, s)

def nCr(n, s): #조합 계산 함수
    num = factorial(n, n-s+1)
    factor = factorial(s, 1)
    return num // factor

for i in range(T):
    N, M = map(int,sys.stdin.readline().split())
    print(nCr(M, N))