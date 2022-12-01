def bfs(start_i,start_j):
    count = 1
    queue = [(start_i,start_j)]
    while queue:
        i, j = queue.pop(0)
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < sero and 0 <= nj < garo and graph[ni][nj] == 1:
                count += 1 # 음식물 개수 구하기
                graph[ni][nj] = 0
                queue.append((ni,nj))
    return count

delta = (1,0),(-1,0),(0,1),(0,-1)
sero, garo, food = map(int, input().split())
graph = [[0] * garo for _ in range(sero)]
for _ in range(food):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

max_count = 0
for i in range(sero):
    for j in range(garo):
        if graph[i][j] == 1:
            graph[i][j] = 0 # 0으로 변경
            max_count = max(max_count,bfs(i,j))
print(max_count)