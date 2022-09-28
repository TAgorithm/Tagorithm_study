N = int(input())# N값입력받기

num_list = list(map(int, str(N))) #N을 다 쪼개기

#30의 배수 조건 - 일의 자리가 0이거나 숫자를 다더해서 3의 배수여야함
if (0 not in num_list) or (sum(num_list) % 3 != 0): #0이 없거나 3의배수가 아닌경우 -1출력
    print(-1)
else: #3의 배수인 경우
    num_list.sort(reverse=True) #큰 숫자대로 정렬 -> 일의 자리에 자동으로 0이 오게됨
    print(''.join(map(str, num_list))) #정렬한 숫자 다시 합치기