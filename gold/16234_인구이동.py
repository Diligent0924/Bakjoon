'''
결과 : 인구이동이 없으면 끝낸다 => 기존값을 유지하고 있어야함   
4방향 델타에서 L <= 인구 <= R 이 있는지를 확인한다.
있다면 경계선을 풀어준다. => 어떤 특정 리스트에 담아주는 것이 좋아보인다? 
'''
import sys
input = sys.stdin.readline

def solution(i,j):
    global unite_sum
    unite = [(i,j)]
    queue = [(i,j)]
    while queue:
        i, j = queue.pop()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(graph[i][j] - graph[ni][nj]) <= R:
                visited[ni][nj] = 1
                queue.append((ni,nj))
                unite.append((ni,nj))
                unite_sum += graph[ni][nj] # 해당 인구를 확인한다.
    return unite

N, L, R = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

time = 0
while True:
    time += 1
    visited = [[0] * N for _ in range(N)] # 방문은 항상 바뀔 수 있다.
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 방문을 안했다면 해준다.
                visited[i][j] = 1
                unite_sum = graph[i][j] # 인구의 합을 구해준다.
                unite = solution(i,j)
                if len(unite) == 1:
                    count +=1
                else:
                    popul = unite_sum // len(unite) # 나눈것을 의미한다.
                    for u_i, u_j in unite: # 연합되어있는 index를 넣는다.
                        graph[u_i][u_j] = popul
    
    if count == N*N:
        print(time-1)
        break