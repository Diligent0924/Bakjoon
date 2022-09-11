'''
BFS 문제에서 Graph 형태로 주어진 문제였는데 생각보다 어려웠음
'''
def bfs(S):
    queue = []
    visited = [0] * (N+1)
    queue.append(S)
    visited[S] = 1 # 1로 두고 나중에 각각 -1씩 빼는 방식으로 쓴다.
    while queue:
        node = queue.pop(0)
        connect = []
        for i in nodes[node]:
            connect.append(i)
        while connect:
            node_2 = connect.pop(0)
            if visited[node_2] == 0:
                visited[node_2] = visited[node] + 1
                queue.append(node_2)
    return sum(list(map(lambda x: x-1 if x >= 1 else 0, visited)))


N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

result = [0] * (N+1)
for i in range(1, N+1):
    result[i] = bfs(i)

print(result.index(min(result[1:])))