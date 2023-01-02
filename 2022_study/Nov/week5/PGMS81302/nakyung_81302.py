def check(place):
    ppl = []
    
    # P 자리 좌표 배열에 넣기
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                ppl.append([i, j])
                
    # 좌표 돌면서 체크         
    for x, y in ppl:
        for x2, y2 in ppl:
            distance = abs(x - x2) + abs(y - y2) # 맨해튼 거리 계산하기
            if (distance == 0 or distance > 2): continue # 거리 0이거나 (같은 좌표) 3 이상이면 체크 X
            if (distance == 1):
                return 0
            # 행 같은데 파티션 없는 경우
            elif x == x2 and place[x][int((y+y2)/2)] != 'X':
                return 0
            # 열 같은데 파티션 없는 경우
            elif y == y2 and place[int((x+x2)/2)][y] != 'X':
                return 0
            # 대각선
            elif x != x2 and y != y2:
                if place[x][y2] != 'X' or place[x2][y] != 'X':
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer