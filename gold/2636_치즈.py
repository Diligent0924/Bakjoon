'''
치즈를 기준으로 1개 이상 비어있는 경우에 판단
비어있는 얘가 구멍이 아니라면 0으로 변경하면 됨
 => 4방향을 기준으로 0인 얘를 4방향으로 계속 돌리면서 구멍인지 아닌지를 확인
'''
def solution_2(i,j):
    visited = [[0] * M for _ in range(N)]
    queue = [(i,j)]
    while queue:
        i, j = queue.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = i + di
            nj = j + dj
            if ni == 0 or nj == 0 or ni == N or nj == M:
                return False
            else:
                if not visited[ni][nj] and not graph[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni,nj))
    return True

def solution(i,j):
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and not graph[ni][nj]: # 0인 얘가 있으면
            # 구멍인지 아닌지를 확인한다.
            spot = solution_2(ni,nj)
            if not spot: # 만약 구멍이 아니라면 해당 지점의 치즈를 지운다.
                graph[i][j] = 2

    
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
time = 0
cheeze_list = []
while True:
    time += 1
    cheeze = False
    cheeze_count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                solution(i,j)
    
    # 마킹해둔 것들을 지운다.
    for i in range(N):
        for j in range(M):
            if time == 1:
                if graph[i][j]:
                    cheeze_count += 1
            if graph[i][j] == 1:
                cheeze_count += 1
                cheeze = True
            if graph[i][j] == 2:
                graph[i][j] = 0
    
    cheeze_list.append(cheeze_count)
    
    if not cheeze:
        if time == 1: # time이 1일때가 있다
            print(time)
            print(cheeze_list.pop())
        else:
            print(time)
            cheeze_list.pop()
            print(cheeze_list.pop())
        break
    # print(cheeze_list)