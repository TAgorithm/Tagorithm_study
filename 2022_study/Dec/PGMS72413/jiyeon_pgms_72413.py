#질문하기 참고해서 풀었음!

def Floyd(distance, s, a, b, n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    min = INF
    for i in range(1, n+1):
        if a == i: #a를 거쳐 가는 경우
            if min > distance[s][i] + distance[i][b]:
                min = distance[s][i] + distance[i][b]
        elif b == i: #b를 거쳐가는 경우
            if min > distance[s][i] + distance[i][a]:
                min = distance[s][i] + distance[i][a]
        else: #a와 b가 아닌 다른 곳을 거쳐가는 경우
            if min > distance[s][i] + distance[i][a] + distance[i][b]:
                min = distance[s][i] + distance[i][a] + distance[i][b]

    if min > distance[s][a] + distance[s][b]: #거쳐가지 않고 따로 가는 경우
        min = distance[s][a] + distance[s][b]
    
    return min

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
n, s, a, b = 6, 4, 6, 2

# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# n, s, a, b = 7, 3, 4, 1

# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# n, s, a, b = 6, 4, 5, 6


global INF
INF = int(1e9)
graph = [[INF for j in range(n+1)] for i in range(n+1)]
for start, end, fare in fares:
    graph[start][end] = fare
    graph[end][start] = fare

print(Floyd(graph, s, a, b, n))