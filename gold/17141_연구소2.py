'''
순열과 조합에 대해서 정확하게 알  필요가 있다.
순열 : 순서가 상관있는것
조합 : 순서가 상관없는것
=> 이 문제는 조합으로 문제를 풀어야함 : 조합문제풀이 => subset구하기
'''
# 바이러스가 M개가 될 때의 경우의 수를 구한다.
def subset():
    virus = []
    for i in range(1<<len(virus_spot)):
        temp = []
        for j in range(len(virus_spot)):
            if i & (1<<j):
                temp.append(virus_spot[j])
                if len(temp) > M:
                    return
        if len(temp) == M:
            print(temp)
    return virus

def bfs(queue, time):
    temp = []
    visited = [[0] * N for _ in range(N)]
    while queue:
        i,j = queue.pop()
        for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                temp.append((ni,nj))
                if not graph[ni][nj]:
                    graph[ni][nj] = 4
                elif graph[ni][nj] == 2:
                    graph[ni][nj] = 5

    # queue가 한번 다 돌고 나서 확인한다.
    for i in range(N):
        for j in range(N):
            if not graph[i][j]:
                if not temp: # 0인데 temp 또한 없다면
                    result = -1
                    return
                else:
                    bfs(temp, time+1) # 1번만 도
                    return




N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 바이러스가 퍼질 수 있는 곳을 찾는다.
virus_spot = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_spot.append((i,j))
#subset
subset()