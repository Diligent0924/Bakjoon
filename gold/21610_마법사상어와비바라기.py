dir = [0,(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)] # 초기상태의 cloud
for _ in range(M):
    # print('start')
    # print(f'cloud:{cloud}')
    # print(graph)
    di, si = map(int, input().split())
    past_cloud = [] # 구름이 있었던 곳을 넣기 위해서 사용한다.
    # 구름의 방향으로 옮긴다. (구름이 다같이 한번에 움직여야한다.)
    for i,j in cloud:
        ni = (i + dir[di][0]*si)%N
        nj = (j + dir[di][1]*si)%N
        graph[ni][nj] += 1 # 해당 위치에서 비가 내린다.(먼저 비가 내린다.)
        past_cloud.append((ni,nj))

    for i,j in past_cloud:
        # 해당 위치에서 대각선 방향으로 확인한 뒤 추가적으로 비가 찬다.
        count = 0
        for k, h in ((-1,1),(1,1),(-1,-1),(1,-1)):
            ki = i + k
            hj = j + h
            if 0 <= ki < N and 0 <= hj < N and graph[ki][hj]: # 만약 있으면
                count += 1
        graph[i][j] += count

    cloud = [] # 모든 구름을 없앤다.
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (i,j) not in past_cloud:
                graph[i][j] -= 2
                cloud.append((i,j))

result = 0
for i in range(N):
    for j in range(N):
        result += graph[i][j]

print(result)

