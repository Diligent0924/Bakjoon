def bfs(start):
    start_node = arr[start]
    queue = []
    queue.extend(start_node)
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(arr[node])
    return visited


N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(N):
    list_a = list(map(int, input().split()))
    for j in range(N):
        if list_a[j]:
            arr[i+1].append(j+1)

result = [[0] * N for _ in range(N)]
for i in range(1, N+1):
    visited = bfs(i)
    for j in visited:
        result[i-1][j-1] = 1

for i in result:
    print(*i)