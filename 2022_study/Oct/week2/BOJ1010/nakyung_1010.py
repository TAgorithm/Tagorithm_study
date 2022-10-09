from math import factorial
import sys
input = sys.stdin.readline

num = int(input()) # 테스트케이스 개수

for i in range(num):
    n, m = map(int, input().split()) # 입력 받기

    # mCn 계산하기
    print(int(factorial(m) / (factorial(m-n) * factorial(n))))