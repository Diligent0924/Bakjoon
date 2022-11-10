N = int(input())
delta = [(0,3),(3,0),(3,-3),(3,3)]
graph = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] != '.':
            if (0 <= i+2 < N and graph[i][j] == graph[i+1][j] == graph[i+2][j]) or (0 <= j+2 < N and graph[i][j] == graph[i][j+1] == graph[i][j+2]) or (0<= i+2 < N and 0<=j+2<N and graph[i][j] == graph[i+1][j+2] == graph[i+2][j+2]) or (0<=i+2<N and 0<=j-2<N and graph[i][j] == graph[i+1][j-1] == graph[i+2][j-2]):
                print(graph[i][j])
                quit()
print('ongoing')
