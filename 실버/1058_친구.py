T = int(input())
graph = [list(input()) for _ in range(T)]
# print(graph)
max_count = 0
for i in range(T):
    visited = [0] * T # 방문했는지를 확인한다.
    for j in range(T):
        if graph[i][j] == "Y":
            visited[j] = 1
            for h in range(T): # 2번째 친구까지 구한다.
                if graph[j][h] == "Y" and not visited[h]:
                    visited[h] = 1
    max_count = max(max_count, visited.count(1)-1)

print(max_count)