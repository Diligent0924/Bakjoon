def bfs(start_i, start_j):
    global visited
    visited[start_i][start_j] = 1
    queue = [(start_i,start_j)]
    while queue:
        i,j = queue.pop(0)
        for di, dj in (0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if graph[ni][nj]:
                    return visited[i][j]
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni,nj))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[0] * M for _ in range(N)] # 방문하는 곳 찾기
for i in range(N):
    for j in range(M):
        if not graph[i][j] and not visited[i][j]:
            print(visited)
            result = max(result, bfs(i,j))
            print(i,j,result)
print(result)
