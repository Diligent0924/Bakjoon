import heapq
def dijkstra():
    visited = [1000000] * (V+1)
    queue = [(0,S)]
    while queue:
        weight, node = heapq.heappop(queue)
        if weight < visited[node]:
            visited[node] = weight
            for x in db[node]:
                w, n = x
                heapq.heappush(queue,(weight+w,n))
    return visited

V, E = map(int, input().split())
S = int(input())
db = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    db[u].append((w,v))

result = dijkstra()[1:]
for i in result:
    if i == 1000000:
        print("INF")
    else:
        print(i)