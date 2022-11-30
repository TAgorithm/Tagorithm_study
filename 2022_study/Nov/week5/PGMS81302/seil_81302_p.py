'''
2021 카카오 채용연계형 인턴십: 거리두기 확인하기
5:50-6:15 (O)

파티션 없으면 
|r1 - r2| + |c1 - c2| < 2 면 탈락

파티션 있으면 고려할 것. 

천천히 로직대로 하면 풀리는 문제.
'''

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = [1] * len(places)


def check(y,x,board):
    # 1. 상 하 좌 우
    dy1 = [-1,+1,+0,+0]
    dx1 = [+0,+0,-1,+1]
    
    # 2. 1 대각선 (좌상 우상 우하 좌하)
    dy2 = [-1,-1,+1,+1]
    dx2 = [-1,+1,+1,-1]
    
    # 3. 2 상 하 좌 우 => *2 해서 진행
    
    for i in range(4):
        ny = y + dy1[i]
        nx = x + dx1[i]
        
        if 0<=ny<5 and 0<=nx<5:
            if board[ny][nx] == "P":
                return False
    
    for i in range(4):
        ny = y + dy2[i]
        nx = x + dx2[i]
    
        if 0<=ny<5 and 0<=nx<5:
            if board[ny][nx] == "P":
                if board[ny][nx - dx2[i]] == "X" and board[ny - dy2[i]][nx] == "X":
                    continue
                else:
                    return False
    
    for i in range(4):
        ny = y + dy1[i] * 2
        nx = x + dx1[i] * 2
        type = "y"
        if dy1[i] == 0:
            type = "x"
        if 0<=ny<5 and 0<=nx<5:
            if board[ny][nx] == "P":
                if type == "y" and board[ny - dy1[i]][nx] != "X":
                    return False
                elif type == "x" and board[ny][nx  - dx1[i]] != "X":
                    return False
    
    
    return True
    
    


for i in range(len(places)):
    exit = False
    board = [["O" for _ in range(5)] for _ in range(5)]
    for j in range(5):
        for k in range(5):
            if places[i][j][k] == "P":
                board[j][k] = "P"
            elif places[i][j][k] == "X":
                board[j][k] = "X"
    
    
    
    
    for j in range(5):
        for k in range(5):
            if board[j][k] == "P":
                if not check(j,k,board):
                    result[i] = 0
                    exit = True
                    break
        
        if exit:
            break
    

print(result)