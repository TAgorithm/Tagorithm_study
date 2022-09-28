# 30(10610) --> 정답
n = int(input())
number, ans = [], []
answer = 0

for i in str(n):
    number.append(i)

number = list(map(int, number))

if 0 in number:
    number.remove(0)

    if sum(number) % 3 == 0:
        number.sort(reverse = True)
        number = list(map(str, number))
        ans = "".join(number)
        answer = int(ans) * 10

    else:
        answer = -1

else:
    answer = -1

print(answer)
