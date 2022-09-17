'''
BFS로 최소거리를 탐색하는 방법에 대하여 알기
'''
def bfs(start_i, start_j):
    queue = []
    queue.append((start_i, start_j))
    visited = [[0] * M for _ in range(N)]
    visited[start_i][start_j] = 1

    while queue:
        i, j = queue.pop(0)
        for di, dj in ((0,1), (0, -1), (1, 0), (-1,0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and graph[ni][nj] == 1:
                visited[ni][nj] = visited[i][j] + 1
                if ni == N-1 and nj == M-1:
                    print(visited[ni][nj])
                    return
                queue.append((ni, nj))



N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
bfs(0,0)