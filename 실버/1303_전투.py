def bfs(start_i,start_j,color):
    global white, black
    queue = [(start_i,start_j)]
    count = 0
    while queue:
        i,j = queue.pop()
        count += 1
        for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
            ni = i + di
            nj = j + dj
            # color가 같고 방문하지 않은 곳이라면 추가해준다.
            if 0 <= ni < sero and 0 <= nj < garo and not visited[ni][nj] and graph[ni][nj] == color:
                visited[ni][nj] = 1
                queue.append((ni,nj))
    # 흑인지 백인지를 확인해서 결과값을 넣어준다.
    if color == "W":
        white += count ** 2
    else:
        black += count ** 2


garo, sero = map(int, input().split())
graph = [list(input()) for _ in range(sero)]
visited = [[0] * garo for _ in range(sero)]
# 각각의 값을 본다.
white = 0
black = 0

for i in range(sero):
    for j in range(garo):
        if not visited[i][j]: # 연결되지 않은 곳이라면 
            visited[i][j] = 1
            bfs(i,j, graph[i][j])

print(white, black)