import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

ac = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            ac.append([i,j])

cnt = [[0 for j in range(M)] for i in range(N)]

def direction(x, y, nx, ny, case):
    if case == 1:
        if (x != nx) and (y == ny):
            if x > nx:
                return -1, 0
            else:
                return 1, 0
        else:
            return -1, -1
    elif case == 2:
        if (x == nx) and (y != ny):
            if y > ny:
                return 0, -1
            else:
                return 0, 1
        else:
            return -1, -1
    elif case == 3:
        if (x == nx)  and (y < ny):
            return -1, 0
        if (x < nx) and (y == ny):
            return 0, -1
        if (x == nx) and (y > ny):
            return 1, 0
        if (x > nx) and (y == ny):
            return 0, 1
    elif case == 4:
        if (x == nx)  and (y < ny):
            return 1, 0
        if (x < nx) and (y == ny):
            return 0, 1
        if (x == nx) and (y > ny):
            return -1, 0
        if (x > nx) and (y == ny):
            return 0, -1
    else:
        return -1, -1

while len(ac) != 0:
    fx = [0, 0, -1, 1]
    fy = [-1, 1, 0, 0]
    x, y = ac.pop()
    cnt[x][y] = 1
    for i in range(4):
        nx = x + fx[i]
        ny = y + fy[i]
        dx = fx[i]
        dy = fy[i]

        while((0 <= nx < N) and (0 <= ny < M)):
            cnt[nx][ny] = 1
            if arr[nx][ny] != 0:
                dx, dy = direction(nx-dx, ny-dy, nx, ny, arr[nx][ny])
                if dx == dy == -1:
                    break
            nx += dx
            ny += dy

count = 0
for s in cnt:
    count += sum(s)
print(count)