from pprint import pprint
N , M = map(int ,input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 해당 위치에서 확인하는 네모로 변경하는 방식 사용하기
def parasite(now_i,now_j, k):
    for q in range(-k, k+1):
        for w in range(-k, k+1):
            ni, nj = now_i + q, now_j + w
            if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] < k:
                graph[ni][nj] = k

# 하나의 parasite로 연결되었는지를 확인하는 방식 (1번만 하면 된다.)
def verify(now_i,now_j):
    queue = [(now_i,now_j)]
    revisited[now_i][now_j] = 0
    while queue:
        i, j = queue.pop(0)
        for di, dj in (0,1),(0,-1),(1,0),(-1,0):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and revisited[ni][nj]:
                queue.append((ni,nj))
                revisited[ni][nj] = 0

    for i in range(N):
        for j in range(M):
            if revisited[i][j]:
                return False
    return True

count = 0
# 확산하는 것을 확인하기
while True:
    # pprint(graph)
    value = set() # 거리가 짧은 순서대로 먼저 진행해야하므로
    visited = [[0] * M for _ in range(N)] # 기존 방문한 것을 중심으로 확인하기
    revisited = [[0] * M  for _ in range(N)] # 1개로 엮여져 있는지를 확인하기
    for i in range(N):
        for j in range(M):
            if graph[i][j]: # 만약 어떤 미생물이 들어있는 경우에
                visited[i][j] = 1
                revisited[i][j] = 1
                value.add(graph[i][j]) 
    istry = True
    for i in range(N):
        for j in range(M):
            if graph[i][j]: # 만약 어떤 값이 들어가있는 경우에
                if istry:
                    b = verify(i,j)
                    istry = False
                    if b:
                        print(count)
                        exit()
    # print("visited")
    # pprint(visited)
    # print(value)
    count += 1
    for v in sorted(list(value)):
        for i in range(N):
            for j in range(M):
                if graph[i][j] and visited[i][j] and graph[i][j] == v: # 어떤 값이 있다면
                    parasite(i,j,graph[i][j]) # 현재를 기준으로 확인하기
                    visited[i][j] = 0
                    if istry:
                        b = verify(i,j)
                        istry = False
                        if b:
                            print(count)
                            exit()
    pprint(graph)
    print("-------------")