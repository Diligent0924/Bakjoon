'''
벽 3개를 둘 수 있는 모든 경우의 수를 구한다.
벽을 전부 둔 후에 바이러스가 계속 퍼지게 둔다. (bfs)
'''
from collections import deque
from copy import deepcopy

def wall(how_many):
    global graph, sero, garo, queue
    if how_many == 3:
        temp_queue = deepcopy(queue)
        bfs(temp_queue)
        return
    else: # 벽이 3개가 될 때까지 돌린다.
        for i in range(sero):
            for j in range(garo):
                if not graph[i][j]:
                    graph[i][j] = 1
                    wall(how_many+1)
                    graph[i][j] = 0

def bfs(queue):
    global result
    visited = []
    queue = queue
    virus_count = 0
    while queue:
        i, j = queue.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < sero and 0 <= nj < garo and not graph[ni][nj]:
                graph[ni][nj] = 1
                virus_count += 1 # 들어가는 개수를 전부 세준다.
                visited.append((ni,nj))
                queue.append((ni,nj))

    # 0인 개수를 찾는다.
    result = max(result, zero_count-virus_count)
    # 기존에 1이였던 것을 0으로 변환시켜준다.
    for i, j in visited:
        graph[i][j] = 0



sero, garo = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(sero)]
queue = deque([])
result = 0
zero_count = 0
# 바이러스가 있는 위치를 확인한다.
for i in range(sero):
    for j in range(garo):
        if graph[i][j] == 2:
            queue.append((i,j))
        elif not graph[i][j]:
            zero_count += 1 # 0의 개수

wall(0)
print(result)