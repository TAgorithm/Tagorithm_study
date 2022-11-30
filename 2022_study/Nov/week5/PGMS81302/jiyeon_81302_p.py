from collections import deque

def bfs(place):
    dq = deque()
    dx = [0,0,1,-1,1,1,-1,-1, 0, 0, 2, -2]
    dy = [1,-1,0,0,1,-1,1,-1, 2, -2, 0, 0]

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                dq.append([i,j])
    
    while(len(dq) != 0):
        x, y = dq.popleft()
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0) and (nx < 5) and (ny >= 0) and (ny < 5):
                if place[nx][ny] == 'P':
                    if nx == x:
                        if abs(ny - y) == 1:
                            return 0
                        if ny < y:
                            y1 = y-1
                        else:
                            y1 = y+1
                        if place[x][y1] != 'X':
                            return 0
                    elif ny == y:
                        if abs(nx - x) == 1:
                            return 0
                        if nx < x:
                            x1 = x-1
                        else:
                            x1 = x+1
                        if place[x1][y] != 'X':
                            return 0
                    else:
                        if (nx > x) and (ny > y):
                            y1 = y+1 
                            x2 = x+1
                        elif (nx > x) and (ny < y):
                            y1 = y-1
                            x2 = x+1
                        elif (nx < x) and (ny > y):
                            y1 = y+1
                            x2 = x-1
                        else:
                            y1 = y-1
                            x2 = x-1
                        if (place[x][y1] != 'X') or (place[x2][y] != 'X'):
                            return 0
                               
    return 1            

place1 = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
place2 = ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
place3 = ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]
place4 = ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]
place5 = ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
place6 = ["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]
place7 = ["PXXPX", "XPXXX", "XXXXP", "XXXXX", "XXXXX"]
place7 = ["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"]
# print(bfs(place1))

# print(bfs(place2))

# print(bfs(place3))

# print(bfs(place4))

# print(bfs(place5))

# print(bfs(place6))

print(bfs(place7))