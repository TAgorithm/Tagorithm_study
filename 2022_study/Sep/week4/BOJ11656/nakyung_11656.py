# 접미사 배열
# 입력된 문자열 받기
s = str(input())

# 빈 리스트 선언
str_list = []

# 문자열 길이만큼 반복
for i in s:
    str_list.append(s) # 리스트에 문자열 하나씩 추가
    s = s[1:]
    
# 결과물 출력
for j in sorted(str_list):
    print(j)        