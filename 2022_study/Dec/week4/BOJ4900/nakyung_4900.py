# 이제는 KeyError가 뜨네...

# 힌트
# 0 -> 063
# 1-> 010
# 2 -> 093
# 3 -> 079
# 4 -> 106
# 5 -> 103
# 6 -> 119
# 7 -> 011
# 8 -> 127
# 9 -> 111

#입력받기
results = [] # 출력 결과 담는 리스트
number = ''
case = ''

# 코드 딕셔너리
codes = {'063': 0, '010': 1, '093': 2, '079': 3, '106': 4, '103': 5, '119': 6, '011': 7, '127': 8, '111': 9}
codes_rev = {value: key for key, value in codes.items()}

while True:
    case = input()
    if (case == "BYE"): break

    # 코드 두 개로 분리하기
    number = case.split('+')
    num1 = number[0]
    num2 = number[1][:-1]

    display1 = '' # 첫 번째 코드 10진수로 변환 (초기화)
    display2 = '' # 두 번째 코드 10진수로 변환 (초기화)

    # 코드 3개씩 나누기, 3개씩 나눈 후에 2진수로 변환
    for i in range(0, len(num1), 3):
        display1 += str(codes[num1[i : i+3]])

    for i in range(0, len(num2), 3):
        display2 += str(codes[num2[i : i+3]])

    displayHab = int(display1) + int(display2)

    # 합한 숫자 한 자리씩 코드로 변환하기
    result = ''
    for i in str(displayHab):
        result += codes_rev[int(i)]
    results.append(case + result)

for result in results:
    print(result)