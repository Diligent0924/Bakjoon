# from pprint import pprint
def bfs(start_i,start_j):
    # print('-------------------')
    # pprint(visited)
    global result
    data = True
    value = graph[start_i][start_j] # 해당 값
    queue = [(start_i,start_j)]
    visited[start_i][start_j] = 1
    # 같은 높이인 경우 하나의 봉우리로 판단하고 더한다.
    while queue:
        i,j = queue.pop(0)
        for di, dj in ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] > value: # 만약 8방향에서 하나라도 넘는게 있다면 끝낸다.
                    data = False
                elif not visited[ni][nj] and graph[ni][nj] == value:
                    visited[ni][nj] = 1
                    queue.append((ni,nj))
    if data:
        print(start_i,start_j)
        result += 1

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]:
            bfs(i,j)
print(result)