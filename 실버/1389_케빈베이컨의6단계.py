def bfs(S):
    queue = []
    visited = []
    queue.append(S)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(nodes[node])
    return visited


N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

print(nodes)

for i in range(1,N):
    print(bfs(i))