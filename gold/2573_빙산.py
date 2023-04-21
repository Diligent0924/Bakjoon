'''
조건 1 : 2 덩어리 이상 분리될 경우 끝낸다.
조건 2 : 주변 기준으로 녹는다.(4방향)

'''
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
bingsans = []
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            bingsans.append((i,j))

result = 0
while True:
    bin_count = 0
    # print(graph)
    # print(bingsans)
    if not bingsans: # 빙산이 다 깎여 있다면 끝낸다.
        print(0)
        break
    else:
        visited = [[0] * M for _ in range(N)]
        remove_list = {}
        for i, j in bingsans:
            if not visited[i][j]: # 방문하지 않는 빙산 위치만 넘어간다.
                bin_count += 1 # 빙산의 개수를 구한다.
                queue = [(i,j)]
                visited[i][j] = 1
                while queue: # 돌아버린다.
                    a, b = queue.pop(0) 
                    for da, db in (0,1),(0,-1),(1,0),(-1,0):
                        na, nb = a + da, b +db
                        if 0 <= na < N and 0 <= nb < M:
                            if not graph[na][nb]: # 만약 옆에 물이 있다면 넣어놓는다.
                                if (a,b) not in remove_list:
                                    remove_list[(a,b)] = 1
                                else:
                                    remove_list[(a,b)] += 1
                            if not visited[na][nb] and graph[na][nb]: # 만약 방문안한 빙산이라면...
                                visited[na][nb] = 1
                                queue.append((na,nb))
        
        # print(remove_list)                
        if bin_count >= 2:
            print(result)
            break
        else:
            for key, value in remove_list.items():
                i,j = key
                t = graph[i][j] - value
                if t <= 0:
                    graph[i][j] = 0
                    bingsans.remove((i,j))
                else:
                    graph[i][j] = t
            result += 1 # 만약 빙산이 1개라면 result를 한개 더한다.