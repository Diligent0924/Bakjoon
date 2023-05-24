'''
전형적인 다익스트라 문제이다.
'''
def bfs():
    queue = [(0,0)]
    while queue:
        i, j = queue.pop(0)
        for di, dj in (1,0),(0,1),(-1,0),(0,-1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                value = visited[i][j] + graph[ni][nj]
                if visited[ni][nj] > value:
                    visited[ni][nj] = value # 해당 값으로 변경한다.
                    queue.append((ni,nj)) # ni,nj 값을 queue에 추가시켜 넣는다.
value = 0
while True:
    N = int(input())
    if not N:
        break
    else:
        value += 1
        graph = [list(map(int, input().split())) for _ in range(N)]
        visited = [[1000000] * N for _ in range(N)]
        visited[0][0] = graph[0][0]
        bfs()
        print(f'Problem {value}: {visited[N-1][N-1]}')
        