N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
delete = []
X_position_i = []
X_position_j = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'X':
            count = 0
            for di, dj in (-1,0),(1,0),(0,1),(0,-1):
                ni, nj = i + di, j + dj
                if 0 > ni or ni >= N or 0 > nj or nj >= M or graph[ni][nj] == '.':
                    count += 1
            if count >= 3:
                delete.append((i,j))
            else:
                X_position_i.append(i)
                X_position_j.append(j)

for i,j in delete:
    graph[i][j] = '.'
# print(graph)
word = ''
for i in range(min(X_position_i),max(X_position_i)+1):
    for j in range(min(X_position_j), max(X_position_j)+1):
        word += graph[i][j]
    print(word)
    word = ''