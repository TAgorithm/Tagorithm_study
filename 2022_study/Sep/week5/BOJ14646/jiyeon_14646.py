N = int(input()) #N값 입력받기

check = [0 for i in range(N)] #돌림판의 칸 수 (N칸)

menulist = list(map(int, input().strip().split())) #메뉴 번호 입력받기

sticker = 0 #스티커의 최대 개수
cnt = 0 #스티커 개수

for menu in menulist:
    if not check[menu-1]: #menu번호가 0이면 스티커를 붙임
        check[menu-1] = 1 #스티커 붙인 표시
        cnt +=1 #스티커 개수 증가
    else: #메뉴 번호가 1이면 스티커가 이미 붙어있음
        check[menu-1] = 0 #스티커 제거 표시
        cnt -= 1 #스티커 개수 감소
    if sticker < cnt: #스티커 최대 개수 구하기
        sticker = cnt

print(sticker) #스티커 최대 개수 출력