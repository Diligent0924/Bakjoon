def bfs(start):
    global count, graph
    queue = []
    queue.append(start)
    graph[start[0]][start[1]] = 0
    while queue:
        i, j = queue.pop(0)
        for di, dj in ((1,0), (0,1), (-1,0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] == 1:
                count += 1
                graph[ni][nj] = 0
                queue.append((ni,nj))
    result_list.append(count)
    return 

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
result_list = []
for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            count = 1
            bfs((a,b))

result_list.sort()
print(len(result_list))
for i in result_list:
    print(i)