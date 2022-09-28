# 10610 (30)
# 7:50 - 8:08

n = input()
sum_n = 0
has_zero = False
ans = ''
for v in n:
    sum_n += int(v)
    if v == '0':
        has_zero = True
    ans += v

if sum_n % 3 == 0 and has_zero == True:
    print(int(''.join(sorted(ans, reverse=True))))
else:
    print(-1)


# 조합문제. -> N이 경우가 너무 많아서. 아니었음.
# 0이 2개인 경우도 있겠구나. 
# - 원래 0을 맨 마지막에 더해주는 식으로 구현함.
# - 0이 여러 개일 수 있겠다고 생각함.
