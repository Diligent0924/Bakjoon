def bfs(start_i, start_j):
    count = 0
    queue = [(start_i,start_j)]
    graph[start_i][start_j] = 1
    while queue:
        count += 1
        i, j = queue.pop(0)
        for di, dj in (0,1),(0,-1),(-1,0),(1,0):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not graph[ni][nj]:
                queue.append((ni,nj))
                graph[ni][nj] = 1
    return count
                
# 밑에서부터 => 0,2, 4,4 => (1,0),()
N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
# print(graph)
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split()) # x2, y2는 하나씩 빼야함
    for i in range(N-y2,N-y1):
        for j in range(x1,x2):
            graph[i][j] = 1

result = []
for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for i in result:
    print(i, end=" ")