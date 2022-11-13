N = int(input())
graph = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] != '.':
            for di, dj in ((0,1),(1,0),(1,1),(1,-1)):
                for h in range(1,3):
                    ni, nj = i + di * h, j + dj * h
                    if 0 <= ni < N and 0 <= nj < N:
                        if graph[ni][nj] != graph[i][j]:
                            break
                    else:
                        break
                else:
                    print(graph[i][j])
                    quit()
print('ongoing')

