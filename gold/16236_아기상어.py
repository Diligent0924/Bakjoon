'''
일단 안에 먹을 수 있는 물고기가 있는지 확인
상어를 기준으로 하나씩 늘려가면서 가장 가까운 것을 찾아낸다.
상어를 해당 지역으로 이동시킨다.
아기상어는 귀엽다.
'''

def end(shark):
    for i in range(N):
        for j in range(N):
            if graph[i][j] < shark and graph[i][j] != 0: #만약 1개 이상 먹이가 있다면
                return True
    return False # 만약 먹이가 없다면

def solution(shark, eat, now_i, now_j, count): # shark:상어의 크기, eat:잡아먹은개수, 
    global result
    # print(f'now_i:{now_i}, now_j:{now_j}, shark:{shark}, count:{count}')
    fin = end(shark)
    if not fin: #먹이가 없을 때
        result = count
        return
    else: # 먹이가 있다면
        queue = [(now_i,now_j)]
        visited = [[0] * N for _ in range(N)]
        visited[now_i][now_j] = 1
        possible = []
        while queue:
            i, j = queue.pop(0) # 가까운 순서대로 해야됨
            for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj]==0:
                    if graph[ni][nj] > shark:
                        continue
                    elif graph[ni][nj] == shark or graph[ni][nj] == 0:
                        visited[ni][nj] = visited[i][j] + 1 # 몇번째인지를 확인해야한다.
                        queue.append((ni,nj))
                    elif graph[ni][nj] < shark and graph[ni][nj] != 0:
                        visited[ni][nj] = visited[i][j] + 1
                        possible.append((ni,nj, visited[ni][nj]))
                        
        if not possible:
            result = count
            return
        # posible에서 가장 가깝다고 생각하는 물고기들의 위치가 나옴
        r_i = 100000
        r_j = 100000
        r_d = 100000
        for f_i, f_j, f_d in possible:
            if f_d < r_d: # 만약 거리면에서 더 가깝다면
                r_i = f_i
                r_j = f_j
                r_d = f_d
            elif f_d == r_d: # 만약 거리상으로 같을 때
                if f_i < r_i: # 물고기가 가장 위쪽인걸 먼저 확인
                    r_i = f_i
                    r_j = f_j
                    r_d = f_d
                elif f_i == r_i: # 만약 물고기의 위쪽이 같은게 여러개면
                    if f_j < r_j:
                        r_i = f_i
                        r_j = f_j
                        r_d = f_d
        # print(r_i,r_j)              
        graph[r_i][r_j] = 0 # 해당 위치로 상어가 이동했다.
        # 먹이를 먹은 후에 cnt에 하나를 추가해주고 만약 shark와 같게되면 0으로 반환
        if eat + 1 == shark:
            solution(shark+1, 0, r_i, r_j, count+r_d-1)
        elif eat + 1 < shark:
            solution(shark, eat+1, r_i, r_j, count+r_d-1)
        
                         

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            graph[i][j] = 0
            solution(shark=2, eat=0, now_i=i, now_j=j, count=0)
print(result)