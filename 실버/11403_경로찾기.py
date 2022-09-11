def bfs(S):
    visited = []
    queue = []
    queue.append(S)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(nodes[node])
    return visited


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

nodes = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            nodes[i+1].append(j+1)
print(nodes)

result = [[0]*N for _ in range(N)]
for i in range(N+1):
    a = bfs(i)
    