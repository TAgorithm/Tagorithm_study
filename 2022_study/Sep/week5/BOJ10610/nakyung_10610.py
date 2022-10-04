# 30의 배수 조건 (10의 배수이자 3의 배수)
# 1. 10의 배수가 되려면 마지막 일의자리 무조건 0으로 끝나야 함. -> 입력값에 0 없으면 -1 출력
# 2. 3의 배수는 각 자리 숫자의 합이 3의 배수이다.

num = str(input())
sum = 0

# 0 없으면 -1 출력
if "0" not in num:
    print(-1)
else:
    for i in range(len(num)):
        sum += int(num[i]) # 각 자리 더해 주기
    
    # 3의 배수가 아니면 -1 출력
    if (sum % 3 != 0):
        print(-1)
    else:
        print("".join(sorted(num, reverse=True))) # 내림차순 정렬 (가장 큰 수)